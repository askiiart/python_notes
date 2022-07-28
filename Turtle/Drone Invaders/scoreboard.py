from turtle import Turtle
import json
from audio import Audio
import time


class Scoreboard(Turtle):

    def __init__(self, x, y):
        """
        Initialize the scoreboard.
        :param x: X coordinate of the scoreboard.
        :param y: Y coordinate of the scoreboard.
        """
        super().__init__()
        self.score = 0

        # Level Data
        with open('level_data.json', 'r') as file:
            self.level_data = json.load(file)

        self.levels = list(self.level_data.keys())
        self.__current_level = 0  # must use dunderscore here because of @property, do not want a setter
        self.__drones_remaining = self.level_data[self.levels[self.current_level]]['NumDrones']
        self.__max_drones = self.level_data[self.levels[self.current_level]]['MaxDrones']
        self.__drone_speed = self.level_data[self.levels[self.current_level]]['DroneSpeed']
        self.__spawn_time = self.level_data[self.levels[self.current_level]]['SpawnTime']

        try:
            with open('data.txt') as file:
                self.high_score = int(file.read())
        except FileNotFoundError:
            self.high_score = 0
        self.color('white')
        self.penup()

        self.hideturtle()
        self.setposition(x, y)
        self.SCORE_FONT = ('Courier', 18, 'bold')
        self.GAME_OVER_FONT = ('Courier', 36, 'bold')
        self.LEFT_ALIGN = 'left'
        self.CENTER_ALIGN = 'center'
        self.draw_scoreboard()

        self.gameover_sound_played = False

    @property
    def current_level(self):
        return self.__current_level

    @property
    def drones_remaining(self):
        return self.__drones_remaining

    @property
    def max_drones(self):
        return self.__max_drones

    @property
    def drone_speed(self):
        return self.__drone_speed

    @property
    def spawn_time(self):
        return self.__spawn_time

    def draw_scoreboard(self):
        self.clear()
        display = (
            f'Score: {self.score} :: Level: {self.current_level + 1} :: Drones Remaining: {self.drones_remaining}'
            f' :: High Score: {self.high_score}')
        self.write(display, align=self.LEFT_ALIGN, font=self.SCORE_FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', 'w') as file:
                file.write(str(self.high_score))
        self.score = 0
        self.draw_scoreboard()

    def game_over(self):
        Audio.stop_music()
        if self.score > self.high_score:
            with open('data.txt', 'w') as file:
                file.write(str(self.score))
            self.score = -1
        if self.current_level == len(self.levels) and self.drones_remaining == 0:
            self.game_over_won()
        else:
            self.game_over_lost()

    def game_over_lost(self):
        self.goto(0, 0)
        self.write('GAME OVER', align=self.CENTER_ALIGN, font=self.GAME_OVER_FONT)
        self.goto(0, -0.15)
        self.write('The world has been destroyed', align=self.CENTER_ALIGN, font=self.GAME_OVER_FONT)
        if not self.gameover_sound_played:
            self.gameover_sound_played = True
            Audio.play_game_lost_sound()

    def game_over_won(self):
        self.goto(0, 0.15)
        self.write('Victory', align=self.CENTER_ALIGN, font=self.GAME_OVER_FONT)
        self.goto(0, 0)
        self.write('You saved the world!', align=self.CENTER_ALIGN, font=self.GAME_OVER_FONT)
        self.goto(0, -0.15)
        self.write('You have been elected', align=self.CENTER_ALIGN, font=self.GAME_OVER_FONT)
        self.goto(0, -0.30)
        self.write('Grand Poobah!', align=self.CENTER_ALIGN, font=self.GAME_OVER_FONT)
        if not self.gameover_sound_played:
            self.gameover_sound_played = True
            Audio.play_game_won_sound()

    def increment(self, amount, droneLost=True):
        self.score += amount
        if droneLost:
            self.__drones_remaining -= 1
        self.draw_scoreboard()

    def new_level(self):
        self.__current_level += 1
        if self.__current_level < len(self.levels):
            self.__drones_remaining = self.level_data[self.levels[self.current_level]]['NumDrones']
            self.__max_drones = self.level_data[self.levels[self.current_level]]['MaxDrones']
            self.__drone_speed = self.level_data[self.levels[self.current_level]]['DroneSpeed']
            self.__spawn_time = self.level_data[self.levels[self.current_level]]['SpawnTime']
            Audio.play_change_level_sound()
            count = 5
            count_down = Turtle()
            count_down.hideturtle()
            count_down.penup()
            count_down.goto(0, 0)
            Audio.pause_music()
            while count >= 0:
                count_down.write(f'{count}', align=self.CENTER_ALIGN, font=self.GAME_OVER_FONT)
                time.sleep(1.0)
                count_down.clear()
                count -= 1
            Audio.unpause_music()
            self.draw_scoreboard()
            return True
        else:
            return False
