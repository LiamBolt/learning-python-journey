from turtle import Screen
import time
from settings import BACKGROUND_COLORS


class Background:
    """
    Manages the game's background appearance with theme cycling functionality.
    Supports multiple themes: day, night, space, and underwater.
    """

    def __init__(self, screen):
        self.screen = screen
        self.current_theme = "day"
        self.transition_duration = 10  # seconds
        self.last_transition = time.time()
        self.apply_theme(self.current_theme)

    def apply_theme(self, theme):
        """
        Applies the specified theme to the game background.
        
        Args:
            theme (str): The theme name to apply
        """
        self.screen.bgcolor(BACKGROUND_COLORS[theme])
        self.current_theme = theme

    def cycle_theme(self):
        current_time = time.time()
        if current_time - self.last_transition >= self.transition_duration:
            themes = list(BACKGROUND_COLORS.keys())
            current_index = themes.index(self.current_theme)
            next_index = (current_index + 1) % len(themes)
            self.apply_theme(themes[next_index])
            self.last_transition = current_time
