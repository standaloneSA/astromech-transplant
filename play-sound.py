#!/usr/bin/env python3

import sys
import os
if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} <mp3>")
    sys.exit(1)

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

from pygame import mixer

mixer.init()
mixer.music.load(sys.argv[1])
mixer.music.play()
