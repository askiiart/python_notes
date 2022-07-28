from boundedturtle import BoundedTurtle
import math
from drone import Drone
from pygame import mixer


class Bomb(BoundedTurtle):
    def __init__(self, init_heading, speed, x_min, x_max, y_min, y_max, scoreboard):
        """
        Initialize the bomb.
        :param init_heading: Heading bomb should travel towards.
        :param speed: Speed of bomb.
        :param x_min: Minimum x coordinate of the screen.
        :param x_max: Maximum x coordinate of the screen.
        :param y_min: Minimum y coordinate of the screen.
        :param y_max: Maximum y coordinate of the screen.
        :param scoreboard: Scoreboard object.
        """
        pass

    def move(self):
        pass

    def distance(self, other):
        p1 = self.position()
        p2 = other.position()
        return math.dist(p1, p2)

    def remove(self):
        pass
