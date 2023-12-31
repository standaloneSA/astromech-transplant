#!/usr/bin/env python3

import sys
import time
from dataclasses import dataclass, field

from gpiozero import Motor
import RPi.GPIO as GPIO

import curses

def go_forward(speed, motors):
    fo

def main():
    print(list_motors())


def old_main(stdscr):
    # Setup the screen
    curses.curs_set(0)
    stdscr.clear()
    stdscr.refresh()

    # Initial position for the cursor
    cursor_x = 0
    cursor_y = 0

    while True:
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        # Read user input
        key = stdscr.getch()

        # Handle arrow keys
        if key == curses.KEY_RIGHT and cursor_x < width - 1:
            cursor_x += 1
        elif key == curses.KEY_LEFT and cursor_x > 0:
            cursor_x -= 1
        elif key == curses.KEY_UP and cursor_y > 0:
            cursor_y -= 1
        elif key == curses.KEY_DOWN and cursor_y < height - 1:
            cursor_y += 1
        elif key == curses.KEY_NPAGE and cursor_y < height - 1:
            cursor_y += height // 2
        elif key == curses.KEY_PPAGE and cursor_y > 0:
            cursor_y -= height // 2
        elif key == ord('q'):
            break  # Exit the program on 'q' key press

        # Print a string at the current cursor position
        stdscr.addstr(cursor_y, cursor_x, "Hello, Arrow Keys and Page Up/Down!")
        stdscr.refresh()

if __name__ == "__main__":
    main()
    #curses.wrapper(main)
