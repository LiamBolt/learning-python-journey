from turtle import Turtle


class Ball(Turtle):
    """
    Represents the game ball, handling movement and collision responses.
    Inherits from Turtle for graphics rendering.
    """

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.position = (0, 0)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Reverses the ball's vertical direction."""
        self.y_move *= -1

    def bounce_x(self):
        """
        Reverses the ball's horizontal direction and increases speed.
        Speed increases by 10% with each paddle hit.
        """
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        """Resets ball to center position with initial speed."""
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
