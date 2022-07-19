import random
import time
from pet import Pet


class Cat(Pet):
    def __init__(self, name='Garfield', color='brown', breed='cat',
                 chance_of_overthrowing_major_world_government=100):  # self is equivalent of this
        """
        Initializes instance of Dog class.
        :param color: color of Dog
        :param breed: breed of Dog
        :param chance_of_overthrowing_major_world_government: the chance of the Cat overthrowing world governments
        """
        # Can add __ before variable name to make it a private
        # variable, so it can't be directly accessed. Only through methods.
        super().__init__(name, color, breed)
        self.__chance_of_overthrowing_major_government = chance_of_overthrowing_major_world_government

    @property
    def chance_of_overthrowing_major_government(self):
        return self.__chance_of_overthrowing_major_government

    @staticmethod
    def __meow():
        print('meow, meow')

    @staticmethod
    def __purr():
        print('*vibration noise between approximately 25 hz and 150 hz*')

    @staticmethod
    def laser():
        Cat.__meow()
        print('*pounce*')
        time.sleep(1)
        print('*pounce pounce*')

    def __str__(self):
        return f'{super().name} is a {super().color} {super().breed} that has a ' \
               f'{self.__chance_of_overthrowing_major_government}% chance of overthrowing a major government.'

    def __eq__(self, other):
        if not isinstance(other, Cat):
            raise TypeError
        if self.color == other.__color and self.__breed == other.__color and \
                self.__chance_of_overthrowing_major_government == other.__color:
            return True
        return False

    @staticmethod
    def make_noise():
        num = random.randint(0, 1)
        if num == 0:
            Cat.__meow()
        else:
            Cat.__purr()
