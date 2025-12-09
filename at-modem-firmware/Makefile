L476RG_MOUNT_DIR = NODE_L476RG
L072Z_MOUNT_DIR = DIS_L072Z
WL55JC_MOUNT_DIR = NOD_WL55JC

ifeq ($(DTLS), 1)
FIRMWARE = firmware-dtls.bin
else
FIRMWARE = firmware.bin
endif

flash-STM32L476-SX1276MB1MAS:
	@cp bin/STM32L476/SX1276MB1MAS/$(FIRMWARE) /media/$(USER)/$(L476RG_MOUNT_DIR)
	@echo "Firmware flashed to the board"

flash-STM32L476-SX1272MB2XAS:
	@cp bin/STM32L476/SX1272MB2XAS/$(FIRMWARE) /media/$(USER)/$(L476RG_MOUNT_DIR)
	@echo "Firmware flashed to the board"

flash-STM32L476-SX1261MB1BAS:
	@cp bin/STM32L476/SX1261MB1BAS/$(FIRMWARE) /media/$(USER)/$(L476RG_MOUNT_DIR)
	@echo "Firmware flashed to the board"

flash-STM32L476-SX1261MB1CAS:
	@cp bin/STM32L476/SX1261MB1CAS/$(FIRMWARE) /media/$(USER)/$(L476RG_MOUNT_DIR)
	@echo "Firmware flashed to the board"

flash-STM32L476-SX1261MB2BAS:
	@cp bin/STM32L476/SX1261MB2BAS/$(FIRMWARE) /media/$(USER)/$(L476RG_MOUNT_DIR)
	@echo "Firmware flashed to the board"

flash-STM32L476-LR1110MB1DxS:
	@cp bin/STM32L476/LR1110MB1DxS/$(FIRMWARE) /media/$(USER)/$(L476RG_MOUNT_DIR)
	@echo "Firmware flashed to the board"

flash-STM32L476-LR1110MB1GxS:
	@cp bin/STM32L476/LR1110MB1GxS/$(FIRMWARE) /media/$(USER)/$(L476RG_MOUNT_DIR)
	@echo "Firmware flashed to the board"

flash-STM32L476-LR1120MB1DxS:
	@cp bin/STM32L476/LR1120MB1DxS/$(FIRMWARE) /media/$(USER)/$(L476RG_MOUNT_DIR)
	@echo "Firmware flashed to the board"

flash-STM32L476-LR1120MB1GxS:
	@cp bin/STM32L476/LR1120MB1GxS/$(FIRMWARE) /media/$(USER)/$(L476RG_MOUNT_DIR)
	@echo "Firmware flashed to the board"

flash-B-L072Z-LRWAN1:
	@cp bin/B-L072Z-LRWAN1/$(FIRMWARE) /media/$(USER)/$(L072Z_MOUNT_DIR)
	@echo "Firmware flashed to the board"
	
flash-NUCLEO-WL55JC1:
	@cp bin/NUCLEO-WL55JC1/$(FIRMWARE) /media/$(USER)/$(WL55JC_MOUNT_DIR)
	@echo "Firmware flashed to the board"
