from elevator import Elevator, State


class Manager:
    def __init__(self, number):
        self.elevators = []
        self.number = number
        self.init_elevators()

    def init_elevators(self):
        for el in range(self.number):
            self.elevators.append(Elevator())
