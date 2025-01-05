from paddle import Paddle
from settings import Difficulty
import random


class AIOpponent(Paddle):
    """
    AI-controlled paddle that predicts ball movement and responds accordingly.
    Inherits from the base Paddle class and implements intelligent movement behavior.
    """

    def __init__(self, position):
        super().__init__(position)
        self.difficulty = Difficulty.MEDIUM

    def move(self, ball):
        prediction = self.predict_ball_position(ball)
        if prediction > self.ycor() + 10:
            self.go_up()
        elif prediction < self.ycor() - 10:
            self.go_down()

    def predict_ball_position(self, ball):
        """
        Calculates the predicted Y-position where the ball will intersect with
        the AI paddle.

        Args:
            ball (Ball): The game ball object

        Returns:
            float: Predicted Y-coordinate with applied difficulty-based error margin
        """
        # Basic prediction with difficulty-based accuracy
        perfect_prediction = ball.ycor() + (ball.y_move * (abs(self.xcor() - ball.xcor()) / abs(ball.x_move)))
        error_margin = (1 - self.difficulty.value) * 100
        return perfect_prediction + random.uniform(-error_margin, error_margin)
