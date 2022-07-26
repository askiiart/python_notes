from boundedturtle import BoundedTurtle
import math
from drone import Drone
from pygame import mixer


class Bomb(BoundedTurtle):
    def __init__(self, init_heading, speed, x_min, x_max, y_min, y_max, scoreboard):
        pass

    def move(self):
        pass

    def distance(self, other):
        p1 = self.position()
        p2 = other.position()
        return math.dist(p1, p2)

    def remove(self):
        pass
