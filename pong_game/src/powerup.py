from turtle import Turtle
import random
import time

class PowerUp(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.active_powerups = {}
        self.spawn_time = None
        
    TYPES = {
        "GROW": {"color": "green", "duration": 5, "symbol": "⬆"},
        "SHRINK": {"color": "red", "duration": 5, "symbol": "⬇"},
        "SPEED": {"color": "yellow", "duration": 3, "symbol": "⚡"},
        "INVINCIBLE": {"color": "purple", "duration": 4, "symbol": "★"}
    }

    def spawn(self):
        self.powerup_type = random.choice(list(self.TYPES.keys()))
        self.color(self.TYPES[self.powerup_type]["color"])
        x = random.randint(-350, 350)
        y = random.randint(-250, 250)
        self.goto(x, y)
        self.spawn_time = time.time()
        self.showturtle()

    def apply_effect(self, paddle, ball):
        if self.powerup_type == "GROW":
            current_stretch = paddle.shapesize()[0]
            paddle.shapesize(stretch_wid=current_stretch * 1.5)
        elif self.powerup_type == "SHRINK":
            current_stretch = paddle.shapesize()[0]
            paddle.shapesize(stretch_wid=max(1, current_stretch * 0.7))
        elif self.powerup_type == "SPEED":
            ball.move_speed *= 1.5
        elif self.powerup_type == "INVINCIBLE":
            paddle.invincible = True
            
        self.active_powerups[self.powerup_type] = {
            "paddle": paddle,
            "start_time": time.time(),
            "duration": self.TYPES[self.powerup_type]["duration"]
        }
        self.hideturtle()

    def update_effects(self):
        current_time = time.time()
        expired_powerups = []
        
        for powerup_type, data in self.active_powerups.items():
            if current_time - data["start_time"] >= data["duration"]:
                self.remove_effect(powerup_type, data["paddle"])
                expired_powerups.append(powerup_type)
                
        for powerup in expired_powerups:
            del self.active_powerups[powerup]

    def remove_effect(self, powerup_type, paddle):
        if powerup_type == "GROW" or powerup_type == "SHRINK":
            paddle.shapesize(stretch_wid=5)  # Reset to original size
        elif powerup_type == "SPEED":
            paddle.move_speed = INITIAL_BALL_SPEED
        elif powerup_type == "INVINCIBLE":
            paddle.invincible = False 