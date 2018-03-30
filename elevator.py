from typing import List

class State:
    STOP = 0
    MOVING = 1
    OVERLOADED = 2
    BROKEN = 3
    IDLE = 4


class Elevator:

    MAX_SPEED = 1.0  # m/sec
    MAX_LOAD = 400  # kg
    ACCELERATION = 2.0  # m/sec^2
    DECELERATION = 0.5  # m/sec^2
    FLOOR_HEIGHT = 3.0  # meters
    STOP_TIMEOUT = 5.0  # sec
    NUM_OF_FLOORS: int = 28
    AVG_HUMAN_WEIGH = 70.0 # kg

    def __init__(self):
        self.is_ok = True
        self.altitude = 0
        self.speed = 0
        self.load = 0
        self.state = State.STOP
        self.queue = []
        self.current_floor = 1
        self.buttons: List[bool] = [False] * self.NUM_OF_FLOORS

    def is_overloaded(self):
        return self.load > self.MAX_LOAD

    def add_floor(self, floor):
        if self.current_floor != floor and floor not in self.queue:
            self.queue.append(floor)
        # Todo: improve algorithm, sort queue

    def handle_stop(self):
        self.queue.remove(self.current_floor)

    def handle_press_button(self, floor):
        self.buttons[floor] = True

    def can_load(self):
        return self.load + self.AVG_HUMAN_WEIGH < self.MAX_LOAD


