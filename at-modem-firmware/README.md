# Lab.SCHC AT-Modem Firmware

This repository contains a pre-built **AT Modem binary** firmware for your development board. There are two options for flashing:

1. Using the provided `Makefile` to flash the firmware.
2. Manually dragging and dropping the `.bin` file to your device's directory.

## Prerequisites

Before proceeding with either method, ensure that your development board is properly **mounted on your filesystem** and accessible.

* Ubuntu
* Serial port terminal (like [minicom](https://manpages.ubuntu.com/manpages/focal/man1/minicom.1.html))

### Hardware

One of the following kits can be used:

* [STM32L476 board](https://os.mbed.com/platforms/ST-Nucleo-L476RG) with those following LoRa shields: 
  * [Semtech SX1276 MB1MAS development kit](https://www.semtech.com/products/wireless-rf/lora-connect/sx1276mb1mas)
  * [Semtech SX1272 MB2xAS development kit](https://www.semtech.com/products/wireless-rf/lora-connect/sx1272mb2das)
  * [Semtech SX1261 MB1BAS development kit](https://www.semtech.com/products/wireless-rf/lora-connect/sx1261dvk1bas)
  * [Semtech SX1261 MB1CAS development kit](https://www.semtech.com/products/wireless-rf/lora-connect/sx1261dvk1cas)
  * [Semtech SX1261 MB2BAS development kit](https://www.semtech.com/products/wireless-rf/lora-connect/sx1261mb2bas)
  * [Semtech LR1110 MB1DxS development kit](https://www.semtech.com/products/wireless-rf/lora-edge/lr1110dvk1tcks)
  * [Semtech LR1110 MB1GxS development kit](https://www.semtech.com/products/wireless-rf/lora-edge/lr1110dvk1tgks)
  * [Semtech LR1120 MB1DxS development kit](https://www.semtech.com/products/wireless-rf/lora-edge/lr1120dvk1tcks)
  * [Semtech LR1120 MB1GxS development kit](https://www.semtech.com/products/wireless-rf/lora-edge/lr1120dvk1tgks)
* [B-L072Z-LRWAN1 board](https://www.st.com/en/evaluation-tools/b-l072z-lrwan1.html)
* [NUCLEO-WL55JC1 board](https://www.st.com/en/evaluation-tools/nucleo-wl55jc.html)

## Option 1: Flashing using Makefile

Connect the development kit to the computer and execute the following command from the repository root directory:

```sh
make flash-<board>-<shield>
```

Where `<board>` can be one of the following:
* `STM32L476`
* `B-L072Z-LRWAN1` (in which case `<shield>` will not be specified)
* `NUCLEO-WL55JC1` (in which case `<shield>` will not be specified)

and `<shield>` can take one the following values:

* `SX1276MB1MAS`
* `SX1272MB2XAS`
* `SX1261MB1BAS`
* `SX1261MB1CAS`
* `SX1261MB2BAS`
* `LR1120MB1DxS`
* `LR1120MB1GxS`
* `LR1110MB1DxS`
* `LR1110MB1GxS`

**Example:** ATModem targeting STM32L476 board and SX1276MB1MAS shield:

```sh
make flash-STM32L476-SX1276MB1MAS
```

In order to check the firmware has been correctly flashed on the board, you can connect in serial using `minicom`:

```sh
minicom -D /dev/ttyACM0 -b 9600 -w
```

Then, the serial terminal should answer to the following AT command:

```sh
AT
OK
```

### AT Modem firmware with DTLS security

A version of the firmware embedding DTLS security is also provided for some of the targets, called `firmware-dtls.bin`.

In order to flash this version, run:

```sh
DTLS=1 make flash-<board>-<shield>
```

The supported platforms are:

* `STM32L476` board with one of the following shields: `LR1110`/`LR1120`/`SX1261`/`SX1272`/`SX1276`.

## Option 2: Drag and Drop the binary

1. Locate the appropriate `.bin` file in the repository (`bin/<board>/<shield>/`)
2. Ensure your development board is mounted and appears as a filesystem on your computer.
3. Drag and drop the `firmware.bin` file directly into the mounted device directory using your file manager of choice.

## AT Modem documentation

The AT Modem documentation is available [here](https://lab-schc.gitlab.io/docs/4-Manual/2-atmodem/).

## Troubleshooting

1. Make sure the board is mounted onto the computer's filesystem. It should appear as a directory in `/media/$USER/`.
2. If the device is properly mounted, edit the corresponding variable within the `Makefile` to make sure the mount directory name matches that of your board's:
  ```  
  <board>_MOUNT_DIR = <mount directory>
  ```

## Used LoRaWAN L2 stack

List of LoRaWAN L2 used in the firmware:

* [STM32L476 board] with the following LoRa shields: 
  * [Semtech SX1272 MB2xAS shield]
  * [Semtech SX1276 MB1MAS shield]
    * uses 4.6.0 Semtech LoRaMac-node L2 with LoRaWAN L2 1.0.4 stack
  * [Semtech SX1261 shields]
    * uses 2.0.1 Semtech LoRa Basics Modem  L2 with LoRaWAN L2 1.0.4 stack
  * [Semtech LR1110 and LR1120 shields]
    * uses 2.0.1 Semtech LoRa Basics Modem  L2 with LoRaWAN L2 1.0.4 stack
* [B-L072Z-LRWAN1 board]
    * uses 4.4.7 Semtech LoRaMac-node L2 with LoRaWAN L2 1.0.3 stack.
* [NUCLEO-WL55JC1 board]
    * uses 4.5.2 Semtech LoRaMac-node L2 with LoRaWAN L2 1.0.4 stack.

## Third-party licences

List of software components used in this repository:

* Lab.SCHC FullSDK - [MIT](LICENCE)

* AT command stack - [SLA0044](https://www.st.com/content/ccc/resource/legal/legal_agreement/license_agreement/group0/87/0c/3d/ad/0a/ba/44/26/DM00216740/files/DM00216740.pdf/jcr:content/translations/en.DM00216740.pdf)

* tiny sscanf - [SLA0044](https://www.st.com/content/ccc/resource/legal/legal_agreement/license_agreement/group0/87/0c/3d/ad/0a/ba/44/26/DM00216740/files/DM00216740.pdf/jcr:content/translations/en.DM00216740.pdf)

* CMSIS - [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)

* CMSIS Device - [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)

* STM32L4 - STM32WL55JC HAL - [BSD-3-Clause](https://opensource.org/licenses/BSD-3-Clause)

* STM32L4 - STM32WL55JC HAL BSP Components - [BSD-3-Clause](https://opensource.org/licenses/BSD-3-Clause)

* STM32 Utilities - [BSD-3-Clause](https://opensource.org/licenses/BSD-3-Clause)

* LoRa Basics modem - [Revised BSD](https://github.com/Lora-net/SWSD001/blob/master/LICENSE.txt)

* LoRaMac-node - [Revised BSD](https://github.com/Lora-net/LoRaMac-node/LICENSE)

* QCBOR - [BSD-3-Clause](https://opensource.org/licenses/BSD-3-Clause)

* vTAL - [MIT](https://opensource.org/licenses/MIT)

* xxtea-c - [MIT](https://opensource.org/licenses/MIT)
