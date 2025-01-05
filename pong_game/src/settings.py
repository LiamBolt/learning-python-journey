from enum import Enum

# Game Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PADDLE_SPEED = 20
INITIAL_BALL_SPEED = 0.1
POWERUP_SPAWN_INTERVAL = 10  # seconds

# Colors
BACKGROUND_COLORS = {
    "day": "#87CEEB",
    "night": "#000033",
    "space": "#000000",
    "underwater": "#006994"
}

class GameMode(Enum):
    LOCAL_MULTIPLAYER = "local_multiplayer"
    AI_OPPONENT = "ai_opponent"
    ONLINE_MULTIPLAYER = "online_multiplayer"

class Difficulty(Enum):
    EASY = 0.6
    MEDIUM = 0.8
    HARD = 0.95 