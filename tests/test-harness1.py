#!/usr/bin/env python3

from gpiozero import Motor, TonalBuzzer
from gpiozero.tones import Tone
import RPi.GPIO as GPIO
import time
import signal
import sys

m1 = Motor(20, 21)
m2 = Motor(19, 26)

trigger=27
echo=17

tone_pin = 25

def test_motor(motor, speed=1, duration=1, repeat=0):
    count = 0
    while count <= repeat:
        start = time.time()
        while time.time() - start < duration:
            motor.forward(speed=speed)
        motor.stop()
        start = time.time()
        while time.time() - start < duration:
            motor.backward(speed=speed)
        motor.stop()
        count += 1


def initialize_board():
    print("Initializing board...")
    GPIO.setmode(GPIO.BCM)
    return True

def initialize_sensor(echo, trigger):
    GPIO.setup(trigger, GPIO.OUT)
    GPIO.setup(echo, GPIO.IN)

    print("Initializing Sensor")
    GPIO.output(trigger, GPIO.LOW)
    time.sleep(1)
    print("OK")
    return True

def distance(trigger, echo):
    GPIO.output(trigger, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(trigger, GPIO.LOW)

    while not GPIO.input(echo):
        pass
    start_time = time.time()
    while GPIO.input(echo):
        pass
    end_time = time.time()

    duration = end_time - start_time
    # Sound has a speed of 34300cm/s and
    # a round trip is twice that
    return round(duration * 17150, 2)

def test_distance(trigger, echo, duration=1):
    speaker = TonalBuzzer(tone_pin)
    tone = speaker.mid_tone
    start = time.time()
    while time.time() - start < duration:
        speaker.play(tone)
        print(distance(trigger, echo))
        speaker.stop()
        if tone < speaker.max_tone:
            tone += 1
        time.sleep(0.2)


if __name__ == '__main__':
    try:
        initialize_board()
        initialize_sensor(echo, trigger)
        print("Testing Motor 1")
        test_motor(m1, speed=0.25, duration=5)
        print("Testing Motor 2")
        test_motor(m2, speed=0.5, duration=5)

        print("Testing distance sensor")
        test_distance(trigger, echo, duration=10)
    except:
        pass
    finally:
        print("Cleaning up...")
