import random
from turtle import Turtle

from constants import *


class Food(Turtle):
    def __init__(self):
        super().__init__(FOOD_SHAPE)
        self.shapesize(FOOD_SIZE, FOOD_SIZE)
        self.color(FOOD_COLOR)
        self.move()

    def move(self):
        x = random.randint(*X_BOUNDS)
        y = random.randint(*Y_BOUNDS)
        self.penup()
        self.goto(x, y)

    def check_collision(self, snake):
        return snake.head.distance(self) <= 15
