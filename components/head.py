""" State machine and driver for the head control """
from pydantic import BaseModel, Field
from typing import List, Optional
from gpiozero import Motor
import RPi.GPIO as GPIO

class HeadConfig(BaseModel):
    """ Structure for the configuration of the head """
    motor_pins: list[int] = Field(repr=True)
    rotation_speed: Optional[float] = Field(repr=True, default=0.4)
    reversed: Optional[bool] = Field(repr=True, default=False)
    sensor_high_pin: int
    sensor_left_pin: int
    sensor_center_pin: int
    sensor_right_pin: int

class HeadMotor(Motor):
    """ 
    Inherits from the gpiozero motor class
    - Adds right() and left()
    - Adds a reversed argument
    """
    def __init__(self, *args, **kwargs):
        self.reversed = kwargs.get("reversed", False)
        super().__init__(*args, **kwargs)

    def left(self, speed):
        if self.reversed:
            self.backward(speed)
        else:
            self.forward(speed)
    
    def right(self, speed):
        if self.reversed:
            self.forward(speed)
        else:
            self.reverse(speed)

class RotationalSensor:
    """ 
    Represents the rotational sensor module
    """
    HARD_LEFT = 0
    LEFT = 1
    CENTER = 2
    RIGHT = 3
    HARD_RIGHT = 4
    UNKNOWN = 255

    def __init__(self, 
                 high_pin: int, 
                 left_sense: int, 
                 right_sense: int, 
                 center_sense: int,
                 callback: function
                 ):
        bouncetime = 500

        self.high_pin = high_pin
        self.left_pin = left_sense
        self.right_pin = right_sense
        self.center_pin = center_sense

        GPIO.setup(self.high_pin, GPIO.OUT)

        GPIO.setup(self.left_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(self.left_pin, GPIO.RISING, callback=callback, bouncetime=bouncetime)

        GPIO.setup(self.right_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(self.right_pin, GPIO.RISING, callback=callback, bouncetime=bouncetime)

        GPIO.setup(self.center_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(self.center_pin, GPIO.RISING, callback=callback, bouncetime=bouncetime)

    def get_state(self):
        """ 
        Returns the pin state 
        """
        if GPIO.input(self.center_pin) and GPIO.input(self.left_pin):
            return self.HARD_LEFT
        if GPIO.input(self.center_pin) and GPIO.input(self.right_pin):
            return self.HARD_RIGHT
        if GPIO.input(self.center_pin):
            return self.CENTER
        if GPIO.input(self.left_pin):
            return self.LEFT
        if GPIO.input(self.right_pin):
            return self.RIGHT
        return self.UNKNOWN

class Head:
    """ 
    Instantiates the head unit 
    """

    def __init__(self, config: HeadConfig):
        """ 
        config is a dict
        """
        self.config = config
        self.motor = HeadMotor(self.config.motor_pins, reversed=self.config.reversed)
        self.rotator = RotationalSensor(
            high_pin=self.config.sensor_high_pin,
            left_sense=self.config.sensor_left_pin,
            center_sense=self.config.sensor_center_pin,
            right_sense=self.config.sensor_right_pin
        )

        # rotation is stored as an integer from -127 to +127, with 0 at dead center
        self.rotation = None
