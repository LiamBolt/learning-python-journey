import pygame


class SoundManager:
    """
    Handles all game audio, including sound effects and background music.
    Uses pygame.mixer for audio playback management.
    """

    def __init__(self):
        pygame.mixer.init()
        self.sounds = {
            'bounce': pygame.mixer.Sound('assets/sounds/bounce.wav'),
            'score': pygame.mixer.Sound('assets/sounds/score.wav'),
            'powerup': pygame.mixer.Sound('assets/sounds/powerup.wav')
        }
        self.background_music = pygame.mixer.music.load('assets/sounds/background_music.wav')
        self.sound_enabled = True
        self.music_enabled = True

    def play_sound(self, sound_name):
        """
        Plays a sound effect if sound is enabled.
        
        Args:
            sound_name (str): Name of the sound effect to play
        """
        if self.sound_enabled and sound_name in self.sounds:
            self.sounds[sound_name].play()

    def toggle_sound(self):
        self.sound_enabled = not self.sound_enabled

    def toggle_music(self):
        self.music_enabled = not self.music_enabled
        if self.music_enabled:
            pygame.mixer.music.play(-1)  # -1 means loop indefinitely
        else:
            pygame.mixer.music.stop()
