#!/usr/bin/env python3

import serial
import json
from time import sleep

dev = "/dev/ttyS0"
speed = 9600

doc= {
    "hostname": "main-host",
    "val1": 1
}

print(f"Opening port {dev}...")
s = serial.Serial(dev, speed)
print(f"Writing hello...")
s.write(json.dumps(doc).encode())
print(f"Done")
