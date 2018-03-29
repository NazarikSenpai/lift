from unittest import TestCase

from elevator import Elevator


class TestElevator(TestCase):
    elevator = None

    def setUp(self):
        self.elevator = Elevator()

    def test_1(self):
        self.elevator.load = Elevator.MAX_LOAD + 1
        self.assertTrue(self.elevator.is_overloaded())

        self.elevator.load = Elevator.MAX_LOAD - 1
        self.assertFalse(self.elevator.is_overloaded())