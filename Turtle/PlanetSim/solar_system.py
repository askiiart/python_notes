import turtle
import math


class SolarSystem:
    def __init__(self, width, height):
        """
        initializes SolarSystem
        :param width: width of world
        :param height: height of world
        """
        self.__theSun = None
        self.__planets = []
        self.__screen = turtle.Screen()
        self.__screen.setup(width=950, height=950)
        self.__screen.setworldcoordinates(-width / 2, -height / 2, width / 2, height / 2)

    def move_planets(self):
        G = 0.025
        dt = 0.001

        for p in self.__planets:
            p.moveTo((p.coords[0] + dt * p.velocity[0], p.coords[1] + dt * p.velocity[1]))

            radius_x = self.__theSun.x - p.coords[0]
            radius_y = self.__theSun.y - p.coords[1]
            radius = math.sqrt((radius_x ** 2) + (radius_y ** 2))  # Uses pythagorean theorem to find radius

            acc_x = G * self.__theSun.mass * radius_x / radius ** 3  # I don't know,
            acc_y = G * self.__theSun.mass * radius_y / radius ** 3  # I haven't taken physics

            p.velocity = (p.velocity[0] + dt * acc_x, p.velocity[1] + dt * acc_y)

    def add_sun(self, sun):
        self.__theSun = sun

    def add_planet(self, planet):
        self.__planets.append(planet)

    def remove_planet(self, planet_name):
        for p in self.__planets:
            if p.name == planet_name:
                self.__planets.remove(p)

    def show_planets(self):
        for p in self.__planets:
            print(p)

    def freeze(self):
        self.__screen.exitonclick()
