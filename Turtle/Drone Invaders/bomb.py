from boundedturtle import BoundedTurtle
import math
from drone import Drone
from audio import Audio


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
        super().__init__(speed, x_min, x_max, y_min, y_max)

        self.resizemode('user')
        self.color('red', 'red')
        self.shape('circle')
        self.turtlesize(0.25)
        self.setheading(init_heading)
        self.getscreen().tracer(False)
        self.getscreen().ontimer(self.move, 100)
        self.scoreboard = scoreboard

    def move(self):
        self.forward(0.1)
        if self.out_of_bounds():
            self.remove()
        for drone in Drone.get_drones():
            if self.distance(drone) < self.get_speed() and self.isvisible():
                drone.remove()
                self.remove()
                Audio.play_explosion_sound()
                self.scoreboard.increment(4)
        self.getscreen().ontimer(self.move, 100)

    def distance(self, other):
        p1 = self.position()
        p2 = other.position()
        return math.dist(p1, p2)

    def remove(self):
        self.hideturtle()
        self.penup()
        self.clear()
