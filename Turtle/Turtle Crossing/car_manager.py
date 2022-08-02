from car import Car
import random
import turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
CAR_TYPES = [["BlueCarRight.gif", "BrightGreenCarRight.gif", "DarkBlueCarRight.gif",
              "GreenCarRight.gif", "BMW-Z4Right.gif"],
             ["BlueCarLeft.gif", "BrightGreenCarLeft.gif", "DarkBlueCarLeft.gif", "GreenCarLeft.gif", "BMW-Z4Left.gif"]]
STARTING_POSITIONS = [(0, (-350, -205)), (0, (-350, -145)), (0, (-350, -80)),
                      (180, (350, 80)), (180, (350, 145)), (180, (350, 205))]
BASE_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.cars = []
        self.lanes = [0, 1, 2, 3, 4, 5]
        self.last_lane = -1
        for car_shape_list in CAR_TYPES:
            for car_shape in car_shape_list:
                car_shape = 'graphics/' + car_shape
                turtle.register_shape(car_shape)

    def create_car(self):
        # Makes sure don't get 2 cars in a row in same lane
        if len(self.lanes) == 0:
            self.lanes = [0, 1, 2, 3, 4, 5]
        lane = random.choice(self.lanes)
        while lane == self.last_lane:
            lane = random.choice(self.lanes)
        self.lanes.remove(lane)
        self.last_lane = lane

        # Set up the car
        starting_info = STARTING_POSITIONS[lane]
        # Get car type (left or right) by using first index in starting_info, then set random shape (gif) accordingly
        index = 0 if starting_info[0] == 0 else 1
        shape = random.choice(CAR_TYPES[index])
        shape = 'graphics/' + shape

        # Create and add car
        self.cars.append(Car(shape, starting_info[1], starting_info[0], BASE_MOVE_DISTANCE + random.randint(-1, 5)))

    def update_cars(self):
        # Remove cars that are finished going on road (off-screen and not coming back)
        self.cars = [car for car in self.cars if (car.heading() == 0 and car.xcor() < 350)
                     or (car.heading() == 180 and car.xcor() > -350)]
        # Iterate over remaining cars, and move them
        for car in self.cars:
            car.move()

    def is_collision(self, other):
        """

        :param other: A turtle object, or object of a child class of turtle
        :return:
        """
        # Get edges of other
        other_top_edge = other.ycor() + 12
        other_bottom_edge = other.ycor() - 12
        other_left_edge = other.xcor() - 12
        other_right_edge = other.xcor() + 12

        # Check each car for whether the distance between edges overlaps
        for car in self.cars:
            car_top_edge = car.ycor() + 11
            car_bottom_edge = car.ycor() - 11
            car_left_edge = car.xcor() - 20
            car_right_edge = car.xcor() + 20
            # It's mom's spaghetti code
            if (
                    (
                            (other_top_edge - car_bottom_edge > 0 and car_top_edge - other_top_edge > 0)
                            or
                            (car_top_edge - other_bottom_edge > 0 and other_bottom_edge - car_bottom_edge > 0)
                    )
                    and
                    (
                            (other_left_edge - car_left_edge > 0 and car_right_edge - other_left_edge > 0)
                            or
                            (other_right_edge - car_left_edge > 0 and car_right_edge - other_right_edge > 0)
                    )
            ):
                return True
            return False
