from turtle import Screen
from drone import Drone
from lasercannon import LaserCannon
from scoreboard import Scoreboard
import time


class DroneInvaders:
    def __init__(self, x_min, x_max, y_min, y_max):
        """
        Initializes DroneInvaders
        :param x_min: minimum x value for things on screen
        :param x_max: maximum x value for things on screen
        :param y_min: minimum y value for things on screen
        :param y_max: maximum y value from things on screen
        """
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        self.screen = Screen()
        self.screen.title('Drone Invaders - A totally original game')
        self.screen.setworldcoordinates(x_min, y_min, x_max, y_max)
        self.scoreboard = Scoreboard(x_min + 0.1, y_max - 0.2)
        self.delay = 0.1
        self.game_states = {'Intro': 1, 'Playing': 2, 'InterLevel': 3, 'GameOver': 4, 'Pause': 5}
        self.game_state = self.game_states['Intro']
        self.screen.bgcolor('light green')
        self.laser_cannon = LaserCannon(x_min, x_max, y_min, y_max, self.screen, self.scoreboard)

    def play(self):
        self.screen.exitonclick()

    def add_drone(self):
        if len(Drone.get_drones()) < 7:
            Drone(0.01, self.x_min, self.x_max, self.y_min, self.y_max)
        if not self.done:
            self.screen.ontimer(fun=self.addDrone, t=1000)

    def quit(self):
        self.screen.bye()
        exit(0)
