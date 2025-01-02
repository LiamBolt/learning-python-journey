from turtle import Turtle, Screen
import random
from typing import List, Tuple


class Painter:
    def __init__(self, color_list: List[Tuple[int, int, int]],
                 dot_size: int = 20,
                 spacing: int = 50):
        self.turtle = Turtle()
        self.screen = Screen()
        self.color_list = color_list
        self.dot_size = dot_size
        self.spacing = spacing
        self._setup_turtle()

    def _setup_turtle(self):
        """Initialize turtle settings"""
        self.screen.colormode(255)
        self.screen.bgcolor("black")
        self.turtle.hideturtle()
        self.turtle.speed("fastest")
        self.turtle.penup()

    def paint_grid(self, rows: int, cols: int, start_x: int = -200,
                   start_y: int = -200):
        """Paint a grid of colored dots"""
        self.turtle.setposition(start_x, start_y)

        for _ in range(rows):
            self._paint_row(cols)
            # Move to start of next row
            self.turtle.setx(start_x)
            self.turtle.sety(self.turtle.ycor() + self.spacing)

    def _paint_row(self, dots: int):
        """Paint a single row of dots"""
        for _ in range(dots):
            color = random.choice(self.color_list)
            self.turtle.dot(self.dot_size, color)
            self.turtle.forward(self.spacing)

    def finish(self):
        """Wait for click to close"""
        self.screen.exitonclick()
