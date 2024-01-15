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

import RPi.GPIO as GPIO

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

BROWN_PIN=16
RED_PIN=19
ORANGE_PIN=20
YELLOW_PIN=21

# Define the GPIO pins
output_pin = BROWN_PIN # Replace with your desired output pin
input_pins = [RED_PIN, ORANGE_PIN, YELLOW_PIN]  # Replace with your desired input pins

# Set the output pin as an output
GPIO.setup(output_pin, GPIO.OUT)

# Set the input pins as inputs with pull-down resistors
for input_pin in input_pins:
    GPIO.setup(input_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Function to call when any input pin goes high
def check_pins(pin):
    get_state()
        

def get_state():
    if GPIO.input(RED_PIN):
        print("Location: Center")
    if GPIO.input(ORANGE_PIN):
        print("Left of 50%")
    if GPIO.input(RED_PIN):
        print("Right of 50%")

# Add event detection for each input pin
for input_pin in input_pins:
    GPIO.add_event_detect(input_pin, GPIO.RISING, callback=check_pins, bouncetime=500)

try:
    # Set the output pin high
    GPIO.output(output_pin, GPIO.HIGH)

    # Run your main code here

    # Keep the program running
    while True:
        pass

except KeyboardInterrupt:
    # Clean up GPIO configuration
    print("Cleaning up")
    GPIO.cleanup()

