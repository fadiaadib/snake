from constants import *


class Board:
    def __init__(self):
        self.n = SCREEN_HEIGHT/2
        self.s = -SCREEN_HEIGHT/2
        self.w = -SCREEN_WIDTH/2
        self.e = SCREEN_WIDTH/2

    def check_collision(self, snake):
        return (snake.head.xcor() <= self.w
                or snake.head.xcor() >= self.e
                or snake.head.ycor() <= self.s
                or snake.head.ycor() >= self.n)
