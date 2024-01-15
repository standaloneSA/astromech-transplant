#!/usr/bin/env python3

import sys
import os
import time

if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} <mp3>")
    sys.exit(1)

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

from pygame import mixer

mixer.init()
try:
    mixer.music.load(sys.argv[1])
except Exception as err:
    print("Error: Unable to play file")
    sys.exit(1)
mixer.music.play()
while mixer.music.get_busy():
    time.sleep(.1)
