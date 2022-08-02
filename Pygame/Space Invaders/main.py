import pygame, sys
from player import Player
import obstacle
from alien import Alien, UFO
from random import choice, randint
from laser import Laser


class Game:
    def __init__(self):
        pass

    def create_obstacle(self, x_start, y_start, offset_x):
        pass

    def create_multiple_obstacles(self, *offset, x_start, y_start):
        pass

    def alien_setup(self, rows, cols, x_distance=60, y_distance=48, x_offset=70, y_offset=100):
        pass

    def alien_position_checker(self):
        pass

    def alien_move_down(self, distance):
        pass

    def alien_shoot(self):
        pass

    def ufo_timer(self):
        pass

    def collision_checks(self):
        pass

        # alien lasers

        # alien

    def display_lives(self):
        pass

    def display_score(self):
        pass

    def victory_message(self):
        pass

    def loser_message(self):
        pass

    def run(self):
        # update sprite groups
        # draw
        pass


class CRT:
    def __init__(self):
        pass

    def create_crt_lines(self):
        pass

    def draw(self):
        pass


if __name__ == '__main__':
    pass
