from motors import MotorController
from unittest import TestCase

class TestMotor(TestCase):
    def setUp(self):
        self.motor1 = MotorController(pin1=0, pin2=0)

    def test_forward(self):
        self.motor1.forward(speed=1)
        assert self.motor1.speed == 0.01

    def test_stop(self):
        self.motor1.stop()
        assert self.motor1.speed == 0

    def test_reverse(self):
        self.motor1.reverse(speed=1)
        assert self.motor1.speed == 0.01
        self.motor1.state == MotorController.REVERSE