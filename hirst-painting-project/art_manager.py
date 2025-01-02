from painter import Painter
from color_palette import ColorPalette
from utils import setup_logging

logger = setup_logging()


class ArtManager:
    def __init__(self, image_paths: list[str]):
        """Initialize ArtManager with image paths for color extraction"""
        self.image_paths = image_paths
        self.color_palette = ColorPalette()
        self.colors = []
        logger.info("ArtManager initialized")

    def prepare_colors(self):
        """Extract colors from provided images"""
        try:
            self.colors = self.color_palette.extract_colors(self.image_paths)
            logger.info(f"Successfully extracted {len(self.colors)} colors")
        except Exception as e:
            logger.error(f"Error extracting colors: {e}")
            raise

    def create_painting(self, rows: int = 10, cols: int = 10,
                        dot_size: int = 20, spacing: int = 50):
        """Create the painting with specified parameters"""
        try:
            painter = Painter(
                color_list=self.colors,
                dot_size=dot_size,
                spacing=spacing
            )
            painter.paint_grid(rows=rows, cols=cols)
            painter.finish()
            logger.info("Painting completed successfully")
        except Exception as e:
            logger.error(f"Error during painting: {e}")
            raise
