#!/bin/bash

PORT="$1"
FIRMWARE="ESP32_GENERIC-20231227-v1.22.0.bin"
if [ -z "$PORT" ] ; then 
    echo "Usage: $0 <PORT-TO-BOARD>" 
    echo "(port is usually /dev/ttyUSB0 or /dev/ttyUSB1)"
    exit 1
fi

esptool.py --chip auto --port "$PORT" erase_flash

if [ ! -e "$FIRMWARE" ] ; then 
    echo "Unable to find $FIRMWARE - has it been downloaded?"
    exit 1
fi

esptoolpy --chip auto --port /"$PORT" write_flash -z 0x1000 "$FIRMWARE"
