from boundedturtle import BoundedTurtle
import random

class Drone(BoundedTurtle):

    droneList = []     #static variable

    @staticmethod
    def getDrones():
        return [x for x in Drone.droneList if x.__alive]

    @staticmethod
    def destory_all():
        for drone in Drone.droneList:
            drone.remove()
        Drone.droneList = []

    def __init__(self, speed, xMin, xMax, yMin, yMax):
        pass

    def move(self):
        pass

    @property
    def alive(self):
        pass

    def remove(self):
        pass