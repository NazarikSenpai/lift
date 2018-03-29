class State:
    STOP = 0
    MOVING = 1
    OVERLOADED = 2
    BROKEN = 3


class Elevator:

    MAX_SPEED = 1.0
    MAX_LOAD = 400
    ACCELERATION = 2.0
    DECELERATION = 0.5

    def __init__(self):
        self.is_ok = True
        self.altitude = 0
        self.speed = 0
        self.load = 0
        self.state = State.STOP

    def is_overloaded(self):
        return self.load > self.MAX_LOAD
