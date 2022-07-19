import math
import turtle


class Planet:
    def __init__(self, name, radius, mass, distanceFromSun, velocity, color):
        """
        initializes the Planet
        :param name: name of planet
        :param radius: radius of planet
        :param mass: mass of planet
        :param distanceFromSun: distance of planet from the sun
        :param velocity: tuple containing the velocity of the planet in the format (x_velocity, y_velocity)
        :param color: color of planet
        """
        self.__name = name
        self.__radius = radius
        self.__mass = mass
        self.__distance = distanceFromSun
        self.__velocity = velocity
        self.__color = color
        self.__coords = [distanceFromSun, 0]

        self.__pT = turtle.Turtle()
        self.__pT.pensize(1)
        self.__pT.color(self.__color)
        if name == 'earth' or name == 'Earth':
            self.__pT.shape('turtle')
        else:
            self.__pT.shape('circle')
        self.__pT.up()
        self.__pT.goto(self.__coords[0], self.__coords[1])
        self.__pT.down()

    def moveTo(self, new_coords):
        self.__coords = new_coords
        self.__pT.goto(self.__coords[0], self.__coords[1])

    @property
    def velocity(self):
        return self.__velocity

    @velocity.setter
    def velocity(self, vel):
        self.__velocity = vel

    @property
    def coords(self):
        return self.__coords

    @coords.setter
    def coords(self, new_coords):
        self.__coords = new_coords

    def __str__(self):
        return f'{self.__name} at distance {self.__distance}'
