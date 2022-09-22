from turtle import Turtle

FONT = ("Courier", 20, "bold")
GAMEOVER_FONT = ("Courier", 28, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-280, 280 - 15)
        self.delay = 0.1
        self.car_prob = 0.1
        self.display()

    def update_level(self):
        self.level += 1
        self.delay *= 0.9
        self.car_prob *= 1.02
        self.display()

    def display(self):
        self.clear()
        self.write(f'Level: {self.level}', font=FONT)

    def game_over(self):
        self.goto(0, -20)
        self.write('GAME OVER', align='center')
