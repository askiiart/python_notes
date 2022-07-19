class Pet:

    def __init__(self, name, color, breed):
        self.__name = name
        self.__color = color
        self.__breed = breed

    # Can do this to make variables private, but look like public
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def color(self):
        return self.__color

    @property
    def breed(self):
        return self.__breed
