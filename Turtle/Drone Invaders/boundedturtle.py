from abc import abstractmethod
from turtle import Turtle

class BoundedTurtle(Turtle):
    def __init__(self, speed, x_min, x_max, y_min, y_max):
        super().__init__()
        self.__x_min = x_min
        self.__x_max = x_max
        self.__y_min = y_min
        self.__y_max = y_max
        self.__speed = speed

    def out_of_bounds(self):
        x_pos, y_pos = self.position()
        out = False
        if x_pos < self.__x_min or x_pos > self.__x_max:
            out = True
        if y_pos < self.__y_min or y_pos > self.__y_max:
            out = True
        return out

    def below_bottom_bound(self):
        x_pos, y_pos = self.position()
        out = False
        if y_pos < self.__y_min:
            out = True
        return out

    def get_speed(self):
        return self.__speed

    def get_x_min(self):
        return self.__x_min

    def getXMax(self):
        return self.__x_max

    def get_y_min(self):
        return self.__y_min

    def get_y_max(self):
        return self.__y_max

    @abstractmethod
    def remove(self):
        pass

    @abstractmethod
    def move(self):
        pass