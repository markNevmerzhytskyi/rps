import random


class Entity:
    def __init__(self, x, y, name):
        self.name = name
        self.x = x
        self.y = y
        self.direction = [random.uniform(-0.10, 0.10), (random.uniform(-0.10, 0.10))]




