from boundedturtle import BoundedTurtle
import random


class Drone(BoundedTurtle):
    droneList = []  # static variable

    def __init__(self, speed, x_min, x_max, y_min, y_max):
        """
        Initialize the drone.
        :param speed: Speed of drone.
        :param x_min: Minimum x coordinate of the screen.
        :param x_max: Maximum x coordinate of the screen.
        :param y_min: Minimum y coordinate of the screen.
        :param y_max: Maximum y coordinate of the screen.
        """
        super().__init__(speed, x_min, x_max, y_min, y_max)

        self.penup()
        self.getscreen().tracer(False)
        if 'images/Drone64.gif' not in self.getscreen().getshapes():
            self.getscreen().addshape('images/Drone64.gif')

        self.shape('images/Drone64.gif')
        self.resizemode('user')
        self.turtlesize(10, 10, 1)
        x = random.uniform(x_min * 0.9, x_max * 0.9)
        self.goto(x, y_max * 1.1)
        self.setheading(270)
        self.getscreen().tracer(True)

        Drone.droneList = Drone.get_drones()
        Drone.droneList.append(self)
        self.__alive = True

    def move(self):
        """
        Moves the drone.
        """
        self.forward(self.get_speed())
        if self.below_bottom_bound():
            return True
        return False

    def remove(self):
        self.__alive = False
        self.hideturtle()

    @property
    def alive(self):
        return self.__alive

    @staticmethod
    def destory_all():
        """
        Destroy all drones.
        :return: None
        """
        for drone in Drone.droneList:
            drone.remove()
        Drone.droneList = []

    @staticmethod
    def get_drones():
        """
        :return: List of alive drones.
        """
        return [x for x in Drone.droneList if x.__alive]
