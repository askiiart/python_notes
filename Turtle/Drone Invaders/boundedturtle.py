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
        xPos, yPos = self.position()
        out = False
        if xPos < self.__xMin or xPos > self.__xMax:
            out = True
        if yPos < self.__yMin or yPos > self.__yMax:
            out = True
        return out

    def below_bottom_bound(self):
        x_pos, y_pos = self.position()
        out = False
        if y_pos < self.__yMin:
            out = True
        return out

    def get_speed(self):
        return self.__speed

    def get_x_min(self):
        return self.__xMin

    def getXMax(self):
        return self.__xMax

    def getYMin(self):
        return self.__yMin

    def getYMax(self):
        return self.__yMax

    @abstractmethod
    def remove(self):
        pass

    @abstractmethod
    def move(self):
        pass