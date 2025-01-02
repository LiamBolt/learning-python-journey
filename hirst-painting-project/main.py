from color_palette import ColorPalette
from painter import Painter


def main():
    # Initialize color palette and extract colors from both images
    palette = ColorPalette()
    colors = palette.extract_colors([
        "spot_painting.jpg",
        "image.jpg"
    ])

    # Create painter with combined color palette
    painter = Painter(
        color_list=colors,
        dot_size=20,
        spacing=50
    )

    # Create the painting
    painter.paint_grid(rows=10, cols=10)
    painter.finish()


if __name__ == "__main__":
    main()
