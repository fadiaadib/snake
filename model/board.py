from constants import *


class Board:
    def __init__(self):
        self.n = SCREEN_HEIGHT - BOARD_GAP
        self.s = -SCREEN_HEIGHT + BOARD_GAP
        self.w = -SCREEN_WIDTH + BOARD_GAP
        self.e = SCREEN_WIDTH - BOARD_GAP

    def check_collision(self, snake):
        return (snake.head.xcor() < self.w
                or snake.head.xcor() > self.e
                or snake.head.ycor() < self.s
                or snake.head.ycor() > self.n)
