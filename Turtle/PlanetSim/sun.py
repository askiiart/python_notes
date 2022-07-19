import math
import turtle


class Sun:
    def __init__(self, name, radius, mass, temp):
        """
        initializes Sun
        :param name: name of Sun
        :param radius: radius of Sun
        :param mass: mass of Sun
        :param temp: temperature of Sun
        """
        self.__name = name
        self.__radius = radius
        self.__mass = mass
        self.__temp = temp
        # List of coordinates in order of [x, y]
        self.__coords = (0, 0)

        self.__sunT = turtle.Turtle()
        self.__sunT.shape('circle')
        self.__sunT.color('orange')
        self.__sunT.shapesize(2)

    @property
    def name(self):
        return self.__name

    @property
    def x(self):
        return self.__coords[0]

    @property
    def y(self):
        return self.__coords[1]

    @property
    def mass(self):
        return self.__mass

    @property
    def radius(self):
        return self.__radius

    @property
    def temperature(self):
        return self.__temp

    @property
    def volume(self):
        return (4 / 3) * math.pi * (self.__radius ** 3)

    @property
    def surface_area(self):
        return 4 * math.pi * (self.__radius ** 2)

    @property
    def density(self):
        return self.__mass / self.volume

    @name.setter
    def name(self, name):
        self.__name = name

    def __str__(self):
        return f'{self.__name} at ({self.__coords[0]}, {self.__coords[1]})'
