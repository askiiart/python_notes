from turtle import Turtle, mainloop


class Etch:
    def __init__(self):
        self.__t = Turtle()
        self.__screen = self.__t.screen
        self.__color_list = ['#35b070', 'black', 'white', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink']
        self.__color_index = 0
        self.__t.color(self.__color_list[self.__color_index])
        self.__t.pensize(1)
        self.__t.speed(0)
        self.__distance = 10
        self.__turn = 10

        # Add callbacks
        self.__screen.onkey(self.__fwd, 'w')
        self.__screen.onkey(self.__back, 's')
        self.__screen.onkey(self.__left, 'a')
        self.__screen.onkey(self.__right, 'd')
        self.__screen.onkey(self.__increase_distance, 'e')
        self.__screen.onkey(self.__decrease_distance, 'q')
        self.__screen.onkey(self.__increase_turn, 'r')
        self.__screen.onkey(self.__decrease_turn, 'f')
        self.__screen.onkey(self.__toggle_pen, 'z')
        self.__screen.onkey(self.__color, 'c')
        self.__screen.onkey(self.__clear, 'x')
        self.__screen.onkey(self.__quit, 'Escape')
        self.__screen.listen()


    def main(self):
        mainloop()

    # Callback methods
    def __increase_distance(self):
        if self.__distance == 100:
            pass
        elif self.__distance < 5:
            self.__distance += 1
        else:
            self.__distance += 5

    def __decrease_distance(self):
        if self.__distance == 1:
            pass
        elif self.__distance <= 5:
            self.__distance -= 1
        else:
            self.__distance -= 5

    def __increase_turn(self):
        if self.__turn == 180:
            pass
        elif self.__turn < 5:
            self.__turn += 1
        else:
            self.__turn += 5

    def __decrease_turn(self):
        if self.__turn == 1:
            pass
        elif self.__turn <= 5:
            self.__turn -= 1
        else:
            self.__turn -= 5

    def __fwd(self):
        self.__t.forward(self.__distance)

    def __back(self):
        self.__t.backward(self.__distance)

    def __left(self):
        self.__t.left(self.__turn)

    def __right(self):
        self.__t.right(self.__turn)

    def __toggle_pen(self):
        if self.__t.isdown():
            self.__t.penup()
        else:
            self.__t.pendown()

    def __clear(self):
        self.__t.clear()

    def __color(self):
        if self.__color_index == 9:
            self.__color_index = -1
        self.__color_index += 1
        self.__t.color(self.__color_list[self.__color_index])

    def __quit(self):
        exit(0)


if __name__ == '__main__':
    draw = Etch()
    draw.main()
