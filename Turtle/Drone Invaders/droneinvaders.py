import turtle
from turtle import Screen
from drone import Drone
from rocket import Rocket
from scoreboard import Scoreboard
import time
from sound_and_music import SoundAndMusic


class DroneInvaders:
    def __init__(self, x_min, x_max, y_min, y_max):
        self.done = None
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
        self.rocket = Rocket(self.x_min, self.x_max, self.y_min, self.y_max, self.screen, self.scoreboard)
        self.delay = 0.1
        self.game_states = {'Intro': 1, 'Playing': 2, 'InterLevel': 3, 'GameOver': 4, 'Pause': 5}
        self.game_state = self.game_states['Intro']

        self.pause_turtle = turtle.Turtle()
        self.pause_turtle.hideturtle()
        self.pause_turtle.penup()
        self.PAUSE_FONT = ('Arial', 24, 'bold')

    def play(self):
        self.scoreboard.draw_scoreboard()
        self.screen.ontimer(self.add_drone, self.scoreboard.spawn_time)

        # Register listeners
        self.screen.onclick(self.rocket.aim)
        self.screen.onkey(self.rocket.shoot, 'space')
        self.screen.onkey(self.rocket.shoot, 's')
        self.screen.onkey(self.pause, 'p')
        self.screen.onkey(self.quit, 'Escape')
        self.screen.onkey(self.quit, 'q')
        self.screen.onkey(self.music_up, 'Up')
        self.screen.onkey(self.music_down, 'Down')
        self.screen.onkey(self.sfx_up, '+')  # Only works with plus on num pad
        self.screen.onkey(self.sfx_down, '=')  # For plus beside backspace
        self.screen.onkey(self.sfx_down, '-')  # Works with either minus
        self.screen.listen()

        self.done = False
        while not self.done:
            self.screen.update()

            if self.game_state == self.game_states['Intro']:
                self.game_state = self.game_states['Playing']
                self.screen.ontimer(self.add_drone, self.scoreboard.spawn_time)
            elif self.game_state == self.game_states['Playing']:
                # Update drones
                if self.scoreboard.drones_remaining <= 0:
                    self.game_state = self.game_states['InterLevel']
                else:
                    for drone in Drone.get_drones():
                        drone.update()
                        if drone.out_of_bounds():
                            Drone.destory_all()
                            self.game_state = self.game_states['GameOver']
                            break
            elif self.game_state == self.game_states['InterLevel']:
                self.screen.ontimer(self.add_drone, 0)
                self.game_state = self.game_states['Playing']
                Drone.destory_all()
                self.rocket.hideturtle()
                if self.scoreboard.new_level():
                    self.rocket.showturtle()
                    self.game_state = self.game_states['Playing']
                    self.screen.ontimer(self.add_drone, self.scoreboard.spawn_time)
                    self.scoreboard.draw_scoreboard()
                else:
                    self.game_state = self.game_states['GameOver']
            elif self.game_state == self.game_states['GameOver']:
                self.screen.ontimer(self.add_drone, 0)
                Drone.destory_all()
                self.rocket.hideturtle()
                self.scoreboard.game_over()
            elif self.game_state == self.game_states['Pause']:
                pass

            time.sleep(self.delay)

        self.screen.exitonclick()

    def add_drone(self):
        if self.game_state != self.game_states['Playing']:
            return
        if self.scoreboard.drones_remaining > len(Drone.get_drones()) and len(
                Drone.get_drones()) < self.scoreboard.max_drones:
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
            self.rocket.hideturtle()
            for drone in Drone.get_drones():
                drone.hideturtle()
            self.draw_pause_message()

        else:
            self.screen.ontimer(self.add_drone, self.scoreboard.spawn_time)
            self.game_state = self.game_states['Playing']
            SoundAndMusic.unpause_music()
            self.rocket.showturtle()
            for drone in Drone.get_drones():
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
        exit(0)
