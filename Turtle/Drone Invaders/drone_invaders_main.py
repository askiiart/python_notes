from droneinvaders import DroneInvaders
import pygame
from pygame import mixer

pygame.init()

mixer.music.load('sounds/mixed_themes.ogg')
mixer.music.set_volume(0.05)
mixer.music.play(loops=-1)


if __name__ == '__main__':
    di = DroneInvaders(-1, 1, -1, 1)
    di.play()
