# import socket programming library
import socket
import time
import base64
import binascii
#from turtle import down
import cbor2 as cbor
import json

# import thread module
from _thread import *
import threading

from flask import Flask
from flask import request
from flask import Response

import requests
import configparser
import os
import sys

from constants import US915, DataRates

'''
chirpstack_server = "http://url:port"
chirpstack_key = "<key>" # openschc-fsdk
'''
config_ini = configparser.ConfigParser()
config_path = os.path.join(os.getcwd(), "resources", "network.ini")
success = config_ini.read(config_path)

if not success:
    print(f"Could not successfully read the config file on path {config_path}")
    sys.exit(1)

http_ip = config_ini["Network"].get("http_ip")
http_port = config_ini["Network"].getint("http_port")
bridge_service_ip = config_ini["Network"].get("bridge_service_ip")
bridge_service_port = config_ini["Network"].getint("bridge_service_port")
schc_gateway_ip = config_ini["Network"].get("schc_gateway_ip")
schc_gateway_port = config_ini["Network"].getint("schc_gateway_port")
ttn_ip = config_ini["Network"].get("ttn_ip")
ttn_downlink_key = config_ini["Network"].get("ttn_downlink_key")

# sock for Writing (uplink handle): send packet to core.py
sock_rw = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock_rw.bind((bridge_service_ip, bridge_service_port))

SF_MTU = [None, #0
          None, #1
          None, #2
          None, #3
          None, #4
          None, #5
          None, #6
          US915.MTU_M[DataRates.DR3],  #7
          US915.MTU_M[DataRates.DR2],  #8
          US915.MTU_M[DataRates.DR1],  #9
          US915.MTU_M[DataRates.DR0],   #10
          None,   #11
          None    #12
          ]

"""
Structure of the exchange, a CBOR structure 

{ # generic values
    1: technology : 1 lorawan, ...
    2: ID (e.g. devEUI in LoRaWAN)
    3: possible MTU # in LoRaWAN regarding the DR the possible frame size
    4: payload 
# informational values regarding the technology
   -1: LoRaWAN SF
   -2: fPort
}

"""

# manage downlink
def recv_data(sock):
    print ("Starting listening")
    while True:
        data, addr = sock_rw.recvfrom(2000)
        print (">>>", binascii.hexlify(data))
        msg = cbor.loads(data)

        if msg[1] != 1:
            print ("not LoraWAN Technology")
            continue

        dev_eui = binascii.hexlify(msg[2]).decode().upper()
        if dev_eui not in app_id:
            print ("device unknown", dev_eui)
            continue

# we are in LoRaWAN technology

        payload = msg[4]

        print (">>", binascii.hexlify(payload))

        fport = payload[0] # first byte is the rule ID
        content = payload[1:]

        if app_id[dev_eui][0] == 'ttn':
 

            print (">>>>", binascii.hexlify(content))

            downlink_msg = {
                "downlinks": [{
                    "f_port":   fport,
                    "frm_payload": base64.b64encode(content).decode()
                }]}
            downlink_url = \
            f"http://{ttn_ip}/api/v3/as/applications/" + \
            app_id[dev_eui][1] + "/devices/" +  app_id[dev_eui][2] + "/down/push"

            headers = {
                'Content-Type': 'application/json',
                'Authorization' : 'Bearer ' + ttn_downlink_key
            }

            print (downlink_url)
            print (downlink_msg)
            print ( headers)

            x = requests.post(downlink_url, 
                                data = json.dumps(downlink_msg), 
                                headers=headers)
            print ("downlink sent", x)

        elif False:#app_id[dev_eui][0] == 'chirpstack':
            print("chirpstack")

            print (">>>>>", binascii.hexlify(content), base64.b64encode(content).decode('utf-8'))

            answer = {
                "deviceQueueItem": {
                    "confirmed": False,
                            "data": base64.b64encode(content).decode('utf-8'),
                    "fPort": fport
                }
            }
            print(answer)

            downlink_url = chirpstack_server + '/api/devices/'+dev_eui+'/queue'
            print (downlink_url)

            headers = {
                "content-type": "application/json",
                "grpc-metadata-authorization" : "Bearer "+ chirpstack_key
            }
            print (headers)

            x = requests.post(downlink_url, data = json.dumps(answer), headers=headers)

            print(x)
        else:
            print ("unknown LNS")
            print (">>>>>>>>>>>>>!!! unknown LNS:", app_id[dev_eui][0])

app_id = {} # contains the mapping between TTN application_id and dev_eui

x = threading.Thread(target=recv_data, args=(1,))
x.start()

app = Flask(__name__)


@app.route('/ttn', methods=['POST']) # API V3 current
def get_from_ttn():
    fromGW = request.get_json(force=True)
    print (fromGW)

    downlink = None
    if "uplink_message" in fromGW and "frm_payload" in fromGW["uplink_message"]:

        payload = base64.b64decode(fromGW["uplink_message"]["frm_payload"])
        #downlink = forward_data(payload)

        message = {
            1 : 1, # Techo LoRaWAN
            2 : binascii.unhexlify(fromGW["end_device_ids"]["dev_eui"]),
            3 : SF_MTU[fromGW["uplink_message"]["settings"]["data_rate"]["lora"]["spreading_factor"]],
            4 : fromGW["uplink_message"]["f_port"].to_bytes(1, byteorder="big") + payload,

            -1: fromGW["uplink_message"]["settings"]["data_rate"]["lora"]["spreading_factor"],
            -2: fromGW["uplink_message"]["f_port"]   
        }
        print (message)
        print (binascii.hexlify(cbor.dumps(message)))
        sock_rw.sendto(cbor.dumps(message), (schc_gateway_ip, schc_gateway_port))

        app_id [fromGW["end_device_ids"]["dev_eui"].upper()] = ["ttn",
                fromGW["end_device_ids"]["application_ids"]["application_id"],
                fromGW["end_device_ids"]["device_id"]
                ]

        print (app_id)


    resp = Response(status=200)
    return resp

'''
@app.route('/chirpstack', methods=['POST']) 
def get_from_chirpstack():
    print("GOT from Chirpstack.")
    fromGW = request.get_json(force=True)
    print (fromGW)


    if "data" in fromGW:
        payload = base64.b64decode(fromGW["data"])
        print(binascii.hexlify(payload))

        dev_eui = base64.b64decode(fromGW["devEUI"])
        fport = fromGW["fPort"]

        print (dev_eui, fport)
        app_id[binascii.hexlify(dev_eui).decode().upper()] = ['chirpstack']

        print (app_id)

        message = {
            1 : 1,
            2 : dev_eui,
            3 : SF_MTU[fromGW["txInfo"]["loRaModulationInfo"]["spreadingFactor"]],
            4 : fport.to_bytes(1, byteorder="big") + payload,

            -1: fromGW["txInfo"]["loRaModulationInfo"]["spreadingFactor"],
            -2 : fport
        }
        print (message)
        print (binascii.hexlify(cbor.dumps(message)))

        sock_w.sendto(cbor.dumps(message), ("127.0.0.1", openschc_port))

    resp = Response(status=200)
    return resp
'''
app.run(host=http_ip, port=http_port)

#y.start()

