import time
from tkinter import TclError
from turtle import Screen

from constants import *
from model.board import Board
from model.snake import TheSnake
from model.food import Food
from model.score_board import ScoreBoard


class Snake:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.screen.bgcolor(BG_COLOR)
        self.screen.title(TITLE)
        self.screen.tracer(0)

        self.snake = TheSnake()
        self.food = Food()
        self.score_board = ScoreBoard()
        self.board = Board()
        self.key_bindings()

        try:
            self.play()
            self.screen.exitonclick()
        except TclError:
            pass

    def key_bindings(self):
        self.screen.listen()
        self.screen.onkey(self.snake.up, 'Up')
        self.screen.onkey(self.snake.down, 'Down')
        self.screen.onkey(self.snake.left, 'Left')
        self.screen.onkey(self.snake.right, 'Right')

    def play(self):
        on = True
        while on:
            time.sleep(REFRESH_PERIOD)
            self.screen.update()
            self.snake.move()

            # Detect collision with food
            if self.food.check_collision(self.snake):
                self.score_board.level_up()
                self.snake.expand_snake()
                self.food.move()

            # Detect collision with wall and tail
            if self.board.check_collision(self.snake) or self.snake.check_tail_collision():
                self.score_board.game_over()
                on = False


if __name__ == '__main__':
    Snake()
