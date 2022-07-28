from turtle import Turtle
from bomb import Bomb
from audio import Audio


class Rocket(Turtle):
    def __init__(self, x_min, x_max, y_min, y_max, screen, scoreboard):
        """
        Initialize the rocket.
        :param x_min: Minimum x coordinate of the screen.
        :param x_max: Maximum x coordinate of the screen.
        :param y_min: Minimum y coordinate of the screen.
        :param y_max: Maximum y coordinate of the screen.
        :param screen: Screen object.
        :param scoreboard: Scoreboard object.
        """
        super().__init__()
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        self.screen = screen
        self.scoreboard = scoreboard

        # Set heading to 90 (pointing up)
        for i in range(0, 360, 10):
            shape = f'rocket{i}.gif'
            if shape not in self.screen.getshapes():
                self.screen.addshape(f'images/rocket/{shape}')
        self.shape(f'images/rocket/rocket90.gif')
        self.setheading(90)

    def aim(self, x, y):
        """
        Set the rocket's heading to point towards the given coordinates.
        :param x: X coordinate.
        :param y: Y coordinate.
        :return: None
        """
        heading = self.towards(x, y)
        heading = int(heading / 10) * 10
        self.setheading(heading)
        self.shape(f'images/rocket/rocket{heading}.gif')

    def shoot(self):
        """
        Shoot a bomb.
        :return: None
        """
        Bomb(self.heading(), 0.1, self.x_min, self.x_max, self.y_min, self.y_max, self.scoreboard)
        Audio.play_laser_sound()
