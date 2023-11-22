from turtle import Turtle
import os

from constants import *


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.load_high_score()

        self.speed('fastest')
        self.color(FONT_COLOR)
        self.penup()
        self.goto(0, SCORE_LOCATION)
        self.hideturtle()
        self.update_scoreboard()

    def load_high_score(self):
        if os.path.exists(SCORE_FILE):
            with open(SCORE_FILE, 'r+') as f:
                self.high_score = int(f.read())

    def save_high_score(self):
        with open(SCORE_FILE, 'w+') as f:
            f.write(str(self.high_score))

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score}      High Score = {self.high_score}",
                   align="center",
                   font=FONT)

    def reset_score(self):
        self.score = 0
        self.update_scoreboard()

    def level_up(self):
        self.score += 1
        self.update_high_score()
        self.update_scoreboard()

    def update_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()

    def game_over(self):
        self.goto(0, 0)
        self.write('Game Over!',
                   align="center",
                   font=BIG_FONT)
