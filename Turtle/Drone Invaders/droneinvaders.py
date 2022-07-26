import turtle
from turtle import Screen
from drone import Drone
from rocket import Rocket
from scoreboard import Scoreboard
import time
from sound_and_music import SoundAndMusic


class DroneInvaders:
    def __init__(self, x_min, x_max, y_min, y_max):
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        self.screen = Screen()
        self.screen.tracer(False)
        self.screen.title('Drone Invaders - Not Space Invaders or Asteroids')
        self.screen.bgcolor('light green')
        self.screen.setworldcoordinates(self.x_min, self.y_min, self.x_max, self.y_max)
        self.scoreboard = Scoreboard(x_min + 0.02, y_max - 0.2)
        self.lasercannon = Rocket(self.x_min, self.x_max, self.y_min, self.y_max, self.screen, self.scoreboard)
        self.delay = 0.1
        self.game_states = {'Intro': 1, 'Playing': 2, 'InterLevel': 3, 'GameOver': 4, 'Pause': 5}
        self.game_state = self.game_states['Intro']

    def play(self):

        self.screen.exitonclick()

    def add_drone(self):
        if self.game_state != self.game_states['Playing']:
            return
        if self.scoreboard.drones_remaining > len(Drone.getDrones()) and len(
                Drone.getDrones()) < self.scoreboard.max_drones:
            Drone(self.scoreboard.drone_speed, self.x_min, self.x_max, self.y_min, self.y_max)
        if not self.done:
            self.screen.ontimer(self.add_drone, self.scoreboard.spawn_time)

    def pause(self):
        if self.game_state == self.game_states['Playing']:
            self.screen.ontimer(self.add_drone, 0)
            self.game_state = self.game_states['Pause']
            SoundAndMusic.pause_music()
            # Write to screen
            # self.pause_screen.bgcolor('light blue')
            self.lasercannon.hideturtle()
            for drone in Drone.getDrones():
                drone.hideturtle()
            self.draw_pause_message()


        else:
            self.screen.ontimer(self.add_drone, self.scoreboard.spawn_time)
            self.game_state = self.game_states['Playing']
            SoundAndMusic.unpause_music()
            self.lasercannon.showturtle()
            for drone in Drone.getDrones():
                drone.showturtle()
            self.pause_turtle.clear()

    def draw_pause_message(self):
        self.pause_turtle.clear()
        up = '⇑'
        down = '⇓'
        self.pause_turtle.color('black')
        self.pause_turtle.goto(-0.5, 0.3)
        self.pause_turtle.write(f'Music volume: {SoundAndMusic.music_volume} of 100', align='left',
                                font=self.PAUSE_FONT)
        self.pause_turtle.goto(-0.5, 0.2)
        self.pause_turtle.write(f'Sfx volume: {SoundAndMusic.sfx_volume} of 100', align='left', font=self.PAUSE_FONT)
        self.pause_turtle.goto(-0.5, 0)
        self.pause_turtle.write(f'Music up {up}', align='left', font=self.PAUSE_FONT)
        self.pause_turtle.goto(-0.5, -0.1)
        self.pause_turtle.write(f'Music down {down}', align='left', font=self.PAUSE_FONT)
        self.pause_turtle.goto(-0.5, -0.2)
        self.pause_turtle.write(f'Sfx up +', align='left', font=self.PAUSE_FONT)
        self.pause_turtle.goto(-0.5, -0.3)
        self.pause_turtle.write(f'Sfx down -', align='left', font=self.PAUSE_FONT)

    def music_up(self):
        SoundAndMusic.change_music_volume(1)
        self.draw_pause_message()

    def music_down(self):
        SoundAndMusic.change_music_volume(-1)
        self.draw_pause_message()

    def sfx_up(self):
        SoundAndMusic.change_sfx_volume(1)
        self.draw_pause_message()

    def sfx_down(self):
        SoundAndMusic.change_music_volume(-1)
        self.draw_pause_message()

    def quit(self):
        self.screen.bye()
        sys.exit()
