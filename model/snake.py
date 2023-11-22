from turtle import Turtle

from constants import *

from random import choice

COLORS = [
    'red',
    'orange',
    'yellow',
    'green',
    'blue',
    'indigo',
    'violet'
]


class TheSnake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        self.expand_snake(SNAKE_INIT_SIZE)

    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def expand_snake(self, count=1):
        for _ in range(count):
            segment = Turtle('square')
            segment.shapesize(SNAKE_SIZE, SNAKE_SIZE)
            segment.color(SNAKE_COLOR)
            # segment.color(choice(COLORS))
            segment.penup()

            if len(self.segments) >= 1:
                tail_x, tail_y = self.segments[-1].pos()
                if self.segments[0].heading() == UP:
                    segment.goto(tail_x, tail_y - SNAKE_SIZE * CONV)
                elif self.segments[0].heading() == DOWN:
                    segment.goto(tail_x, tail_y + SNAKE_SIZE * CONV)
                elif self.segments[0].heading() == RIGHT:
                    segment.goto(tail_x - SNAKE_SIZE * CONV, tail_y)
                elif self.segments[0].heading() == LEFT:
                    segment.goto(tail_x + SNAKE_SIZE * CONV, tail_y)
            else:
                segment.goto(0, 0)

            self.segments.append(segment)

    def move(self):
        for segment in self.segments[:0:-1]:
            prev_segment = self.segments[self.segments.index(segment) - 1]
            segment.goto(prev_segment.pos())
        self.head.forward(SNAKE_SPEED)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def check_tail_collision(self):
        for segment in self.segments[3::]:
            if segment.distance(self.head) < 10:
                return True
        return False
