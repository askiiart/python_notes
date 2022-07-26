from boundedturtle import BoundedTurtle
import random


class Drone(BoundedTurtle):
    droneList = []  # static variable

    def __init__(self, speed, x_min, x_max, y_min, y_max):
        pass

    @staticmethod
    def get_drones():
        return [x for x in Drone.droneList if x.__alive]

    @staticmethod
    def destory_all():
        for drone in Drone.droneList:
            drone.remove()
        Drone.droneList = []

    def move(self):
        pass

    @property
    def is_alive(self):
        pass

    def remove(self):
        pass
