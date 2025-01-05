from turtle import Turtle


class ScoreBoard(Turtle):
    """
    Manages and displays the game score for both players.
    Inherits from Turtle for graphics rendering.
    """

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """Clears and redraws the scoreboard with current scores."""
        self.clear()
        self.goto(-180, 200)
        self.write(f"{self.l_score}", align="center", font=("Courier", 80, "normal"))
        self.goto(180, 200)
        self.write(f"{self.r_score}", align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()