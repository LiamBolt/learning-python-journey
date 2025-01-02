import logging
from typing import Tuple
import os


def setup_logging():
    """Configure logging for the application"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    return logging.getLogger(__name__)


def validate_rgb_color(color: Tuple[int, int, int]) -> bool:
    """Validate if a color tuple contains valid RGB values"""
    if len(color) != 3:
        return False
    return all(0 <= value <= 255 for value in color)


def ensure_directory_exists(path: str):
    """Create directory if it doesn't exist"""
    if not os.path.exists(path):
        os.makedirs(path)
