from abc import abstractmethod
from turtle import Turtle

class BoundedTurtle(Turtle):
    def __init__(self, speed, xMin, xMax, yMin, yMax):
        super().__init__()
        self.__xMin = xMin
        self.__xMax = xMax
        self.__yMin = yMin
        self.__yMax = yMax
        self.__speed = speed

    def outOfBounds(self):
        xPos, yPos = self.position()
        out = False
        if xPos < self.__xMin or xPos > self.__xMax:
            out = True
        if yPos < self.__yMin or yPos > self.__yMax:
            out = True
        return out

    def belowBottomBound(self):
        x_pos, y_pos = self.position()
        out = False
        if y_pos < self.__yMin:
            out = True
        return out

    def getSpeed(self):
        return self.__speed

    def getXMin(self):
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