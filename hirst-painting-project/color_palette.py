import colorgram
from typing import List, Tuple


class ColorPalette:
    def __init__(self):
        self.colors: List[Tuple[int, int, int]] = []

    def extract_colors(self, image_paths: List[str],
                       colors_per_image: int = 30) -> List[Tuple[int, int, int]
                                                           ]:
        """Extract colors from multiple images and combine them."""
        all_colors = set()  # Using set to avoid duplicates

        for image_path in image_paths:
            colors = colorgram.extract(image_path, colors_per_image)
            for color in colors:
                # Only add colors that aren't too close to white
                if not self._is_too_light(color.rgb):
                    all_colors.add((color.rgb.r, color.rgb.g, color.rgb.b))

        self.colors = list(all_colors)
        return self.colors

    def _is_too_light(self, rgb) -> bool:
        """Check if a color is too close to white."""
        return rgb.r > 250 and rgb.g > 250 and rgb.b > 250
