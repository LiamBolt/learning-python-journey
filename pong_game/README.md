# Pong Game

A modern take on the classic Pong game, built with Python and Turtle graphics.

## Features

- Single-player mode with AI opponent
- Local multiplayer mode
- Dynamic background themes
- Power-up system
- Sound effects and background music
- Configurable difficulty levels

## Requirements

- Python 3.7+
- Pygame library

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/pong_game.git
``` 

2. Install required packages:
```bash
pip install -r requirements.txt
``` 

## How to Play

Run the game:
```bash
python src/main.py
``` 

### Controls

- Right Paddle:
  - Up Arrow: Move Up
  - Down Arrow: Move Down

- Left Paddle (in multiplayer mode):
  - W: Move Up
  - S: Move Down

- Other Controls:
  - M: Toggle Sound Effects
  - N: Toggle Background Music

## Project Structure 

pong_game/
├── assets/
│ └── sounds/
│ ├── bounce.wav
│ ├── score.wav
│ ├── powerup.wav
│ └── background_music.mp3
├── src/
│ ├── ai_opponent.py
│ ├── background.py
│ ├── ball.py
│ ├── main.py
│ ├── paddle.py
│ ├── powerup.py
│ ├── scoreboard.py
│ ├── settings.py
│ └── sound_manager.py
├── requirements.txt
└── README.md
```

## License

This project is licensed under the ___ License.