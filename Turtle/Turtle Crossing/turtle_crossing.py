import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard
import random


def soft_exit():
    screen.bye()
    exit(0)


screen = Screen()
screen.setup(width=600, height=600)
screen.bgpic('graphics/highway_lanes.png')
screen.tracer(False)  # Turns off auto screen updates
screen.title('Turtle Crossing - *Definitely* not Frogger')

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

car_manager.create_car()
screen.listen()
screen.onkey(fun=player.move, key='space')  # Listens for 'space' key, and moves
screen.onkey(fun=soft_exit, key='q')

game_is_on = True
# The game loop
while game_is_on:
    time.sleep(scoreboard.delay)

    # Update cars (move the cars)
    car_manager.update_cars()

    # Check if turtle made it across
    if player.ycor() >= FINISH_LINE_Y:
        scoreboard.update_level()
        player.reset_player()

    # Check if another car should be added (10% chance at level 1)
    if random.random() < scoreboard.car_prob:
        car_manager.create_car()

    # Check for collision with car
    if car_manager.is_collision(player):
        scoreboard.game_over()
        game_is_on = False

    screen.update()

screen.exitonclick()
