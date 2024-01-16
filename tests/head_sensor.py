#!/usr/bin/env python3

""" 
Pinout Config for the rotational encoder: 

Brown:
Red:
  low:
  high: Center, 100 left, 100 right
Orange:
  low: 
  high: left of 50%
Yellow: 
  low:
  high: right of 50%
"""
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

from pygame import mixer
import RPi.GPIO as GPIO

from gpiozero import Motor

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

BROWN_PIN=16
RED_PIN=19
ORANGE_PIN=20
YELLOW_PIN=21

# Define the GPIO pins
output_pin = BROWN_PIN # Replace with your desired output pin
input_pins = [RED_PIN, ORANGE_PIN, YELLOW_PIN]  # Replace with your desired input pins


def alert(alertname=""):
    alert_map = {
        "short_sass": "17",
        "emergency": "1",
        "overload": "14",
        "info": "19",
        "bored": "13",
    }
    if alertname in alert_map.keys():
        filename = f"media/astromech_{alert_map[alertname]}.mp3"
    else:
        filename = "media/astromech_18.mp3"

    mixer.music.load(filename)
    mixer.music.play()

# Function to call when any input pin goes high
def check_pins(pin):
    get_state()
        
def show_pins():
    print("####")
    get_state()
    print("Here are the pin states")
    print(f"RED: {str(GPIO.input(RED_PIN))}")
    print(f"ORANGE: {str(GPIO.input(ORANGE_PIN))}")
    print(f"YELLOW: {str(GPIO.input(YELLOW_PIN))}")
    print("")

def get_state():
    if GPIO.input(RED_PIN):
        if GPIO.input(ORANGE_PIN):
            alert("info")
            print("Hard Left")

        elif GPIO.input(YELLOW_PIN):
            alert("info")
            print("Hard Right")
        else:
            alert("short_sass")
            print("Location: Center")
    elif GPIO.input(ORANGE_PIN):
        print("Left of 50%")
    elif GPIO.input(YELLOW_PIN):
        print("Right of 50%")
    else:
        print("Unknown")


def init():
    # Set the input pins as inputs with pull-down resistors
    for input_pin in input_pins:
        GPIO.setup(input_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(input_pin, GPIO.RISING, callback=check_pins, bouncetime=500)

    # Set the output pin as an output
    GPIO.setup(output_pin, GPIO.OUT)


    # Setup sounds
    mixer.init()

if __name__ == '__main__':
    init()
    try:
        # Set the output pin high
        GPIO.output(output_pin, GPIO.HIGH)


        head_motor = Motor(12, 13)

        show_pins()

        while True:
            head_motor.forward(speed=0.1)

    except KeyboardInterrupt:
        # Clean up GPIO configuration
        show_pins()
        print("Cleaning up")
        #GPIO.cleanup()

