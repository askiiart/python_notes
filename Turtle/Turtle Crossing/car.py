from turtle import Turtle


class Car(Turtle):

    def __init__(self, shape, start_position, direction, speed):
        super().__init__(shape)
        self.penup()
        self.goto(start_position)
        self.setheading(direction)
        self.car_speed = speed

    def move(self):
        self.forward(self.car_speed)
