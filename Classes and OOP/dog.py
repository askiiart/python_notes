from pet import Pet


class Dog(Pet):
    def __init__(self, name='Odie', color='brown', breed='poodle', weight=25.0):  # self is equivalent of this
        """
        Initializes instance of Dog class.
        :param name: name of Dog
        :param color: color of Dog
        :param breed: breed of Dog
        :param weight: weight of Dog
        """
        super().__init__(name, color, breed)
        # Can add __ before variable name to make it a private
        # variable, so it can't be directly accessed. Only through methods.
        self.__weight = weight
        self.__bark()

    @staticmethod
    def __bark():
        """
        woof
        :return: None
        """
        print('woof woof')

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.__weight = weight

    def __str__(self):
        return f'{self.name} {self.color} {self.breed} that weighs {self.__weight}.'

    def __eq__(self, other):
        if not isinstance(other, Dog):
            raise TypeError
        if super().color == other.color and super().breed == other.breed and self.__weight == other.__weight:
            return True
        return False

    def do_something(self, **kwargs):
        if 'item' in kwargs:
            self.__bark()
            print(f"Here's a {kwargs['item']}")
        else:
            print('*confusion*')
