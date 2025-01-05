from turtle import Turtle


class Paddle(Turtle):
    """
    Base paddle class for player-controlled or AI-controlled paddles.
    Inherits from Turtle for graphics rendering.
    """

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)

    def go_up(self):
        """Moves the paddle upward by a fixed amount."""
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        """Moves the paddle downward by a fixed amount."""
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
