"""
Provides a motor controller
"""

from gpiozero import Motor

class MockMotor:
    """ Create a generic class with the methods to look like a motor """
    def __init__(self, forward_pin, backward_pin, pwm):
        self.pin1 = forward_pin
        self.pin2 = backward_pin
        self.pwm = pwm
        self.speed = 0
        self.direction = None

    def forward(self, speed):
        """ Set motor forward """
        self.speed = speed
        self.direction = "forward"

    def backward(self, speed):
        """ Set motor backward """
        self.speed = speed
        self.direction = "backward"

    def reverse(self):
        """ Reverse motor direction to the same speed """
        if self.direction == "forward":
            self.backward(self.speed)
        else:
            self.forward(self.speed)

    def stop(self):
        """ Halt the motor """
        self.direction = None
        self.speed = 0

    def is_active(self):
        """ Returns true if the motor has a direction """
        if self.direction:
            return True
        return False

    def value(self):
        """ Returns a float of the speed """
        return self.speed

class MotorController(Resource):
    """ Controls motor """
    IDLE=0
    FORWARD=1
    REVERSE=2

    def __init__(self, pin1:int, pin2:int):
        """ 
        Instantiates a motor 

        pins is a list of integers, however if both are 0, then the motor is
        considered a mocked out motor with no actual hardware.
        """
        # If we're mocked out, then we won't send signals to any pin.
        self.mock = False

        self.pin1 = pin1
        self.pin2 = pin2
        if pin1 == 0 and pin2 == 0:
            self.mock = True

        if not self.mock:
            self.motor = Motor(self.pin1, self.pin2, pwm=True)
        else:
            self.motor = MockMotor(self.pin1, self.pin2, pwm=True)

        self._state = MotorController.IDLE
        self._speed = 0
        super().__init__()

    @property
    def state (self):
        """ Returns the state """
        return self._state

    @property
    def speed(self):
        """ Returns speed of motor """
        return self._speed

    def forward(self, speed=80):
        """ Set the forward speed """
        speed = speed/100
        self.motor.forward(speed=speed)
        self._state = MotorController.FORWARD
        self._speed = speed
        return True

    def stop(self):
        """ Stop the motor """
        self.motor.stop()
        self._state = MotorController.IDLE
        self._speed = 0
        return True

    def reverse(self, speed=20):
        """ Set the reverse speed """
        speed = speed/100
        self.motor.backward(speed=speed)
        self._state = MotorController.REVERSE
        self._speed = speed
        return True
    