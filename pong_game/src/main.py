from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
from powerup import PowerUp
from background import Background
from sound_manager import SoundManager
from ai_opponent import AIOpponent
from settings import GameMode, SCREEN_WIDTH, SCREEN_HEIGHT, POWERUP_SPAWN_INTERVAL
import time


class PongGame:
    """
    Main game class that coordinates all game components and manages the game
    loop.
    Handles initialization, user input, game state, and updates.
    """

    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.screen.title("Enhanced Pong")
        self.screen.tracer(0)
        
        self.background = Background(self.screen)
        self.sound_manager = SoundManager()
        self.scoreboard = ScoreBoard()
        self.ball = Ball()
        self.powerup = PowerUp()
        
        # Initialize game mode
        self.game_mode = GameMode.LOCAL_MULTIPLAYER
        self.setup_players()
        
        self.setup_controls()
        self.sound_manager.toggle_music()
        
    def setup_players(self):
        self.r_paddle = Paddle((350, 0))
        if self.game_mode == GameMode.AI_OPPONENT:
            self.l_paddle = AIOpponent((-350, 0))
        else:
            self.l_paddle = Paddle((-350, 0))

    def setup_controls(self):
        self.screen.listen()
        self.screen.onkey(self.r_paddle.go_up, "Up")
        self.screen.onkey(self.r_paddle.go_down, "Down")
        
        if self.game_mode == GameMode.LOCAL_MULTIPLAYER:
            self.screen.onkey(self.l_paddle.go_up, "w")
            self.screen.onkey(self.l_paddle.go_down, "s")
            
        # Additional controls
        self.screen.onkey(self.sound_manager.toggle_sound, "m")
        self.screen.onkey(self.sound_manager.toggle_music, "n")
        
    def run_game(self):
        game_is_on = True
        last_powerup_spawn = time.time()
        
        while game_is_on:
            self.screen.update()
            time.sleep(self.ball.move_speed)
            self.ball.move()
            self.background.cycle_theme()
            
            # AI opponent movement
            if self.game_mode == GameMode.AI_OPPONENT:
                self.l_paddle.move(self.ball)
            
            # Power-up spawning and management
            current_time = time.time()
            if current_time - last_powerup_spawn >= POWERUP_SPAWN_INTERVAL:
                self.powerup.spawn()
                last_powerup_spawn = current_time
            
            self.powerup.update_effects()
            
            # Collision detection
            self.detect_collisions()
            
            # Update display
            self.screen.update()
            
    def detect_collisions(self):
        """
        Checks and handles all game collisions:
        - Ball with walls
        - Ball with paddles
        - Paddles with power-ups
        Updates score and triggers appropriate sound effects.
        """
        # Wall collisions
        if self.ball.ycor() > 280 or self.ball.ycor() < -280:
            self.ball.bounce_y()
            self.sound_manager.play_sound('bounce')
            
        # Paddle collisions
        if (self.ball.distance(self.r_paddle) < 50 and self.ball.xcor() > 320) or \
           (self.ball.distance(self.l_paddle) < 50 and self.ball.xcor() < -320):
            self.ball.bounce_x()
            self.sound_manager.play_sound('bounce')
            
        # Power-up collisions
        if self.powerup.isvisible():
            for paddle in [self.l_paddle, self.r_paddle]:
                if self.powerup.distance(paddle) < 30:
                    self.powerup.apply_effect(paddle, self.ball)
                    self.sound_manager.play_sound('powerup')
                    
        # Scoring
        if self.ball.xcor() > 380:
            self.ball.reset_position()
            self.scoreboard.l_point()
            self.sound_manager.play_sound('score')
            
        if self.ball.xcor() < -380:
            self.ball.reset_position()
            self.scoreboard.r_point()
            self.sound_manager.play_sound('score')

if __name__ == "__main__":
    game = PongGame()
    game.run_game()
