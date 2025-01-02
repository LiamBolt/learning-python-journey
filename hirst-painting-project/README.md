# Hirst Painting Project

This project recreates the famous "Hirst painting" style using Python and the Turtle graphics library. It demonstrates basic Object-Oriented Programming (OOP) concepts and is designed for intermediate-level learners. The code is modular, reusable, and ready for deployment or extension.

---

## Project Structure

```
hirst_painting_project/
├── main.py               # Entry point of the application
├── painter.py            # Handles the painting logic
├── color_palette.py      # Extracts and manages color palettes
├── art_manager.py        # Coordinates the painting workflow
├── utils.py              # Contains reusable utility functions
├── README.md             # Project documentation
└── test/                 # Unit tests for project components
    ├── test_painter.py
    └── test_color_palette.py
```

---

## Features

1. **Object-Oriented Design**
   - Encapsulates functionality into classes for better modularity and reusability.

2. **Color Palette Management**
   - Extracts RGB colors from an image to create dynamic color schemes.

3. **Customizable Painting**
   - Parameters for canvas size, dot size, and spacing are configurable.

4. **Beginner-Friendly Documentation**
   - Includes detailed comments and docstrings to aid understanding.

---

## Getting Started

### Prerequisites

Ensure you have Python installed (version 3.6 or later). You will also need the following libraries:

- `turtle` (built-in)
- `colorgram` (install via pip)

To install the required packages:

```bash
pip install colorgram.py
```

### Running the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/hirst-painting-project.git
   cd hirst-painting-project
   ```

2. Run the `main.py` file:
   ```bash
   python main.py
   ```

3. Watch the artwork being created on the Turtle graphics screen!

### Project Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Add your source image:
   - Place your `spot_painting.jpg` in the project root directory
   - Or use any other image and update the path in `main.py`

### Testing

Run the tests using pytest:
```bash
pytest
```

Run code quality checks:
```bash
flake8 .
black . --check
```

### Code Style

This project follows:
- PEP 8 style guide
- Black code formatting
- Type hints for better code clarity

---

## How It Works

### Main Components

1. **Painter (`painter.py`)**
   - Manages the Turtle graphics operations.
   - Paints dots and handles movements on the canvas.

2. **Color Palette (`color_palette.py`)**
   - Extracts colors from an input image to generate a palette.

3. **Art Manager (`art_manager.py`)**
   - Orchestrates the painting process by utilizing `Painter` and `ColorPalette`.

### Workflow

- The `ColorPalette` class extracts a list of RGB colors from an image.
- The `Painter` class uses the color list to paint dots on the canvas.
- The `ArtManager` class coordinates the flow and ensures the painting is generated correctly.

---

## Example Output

The project will produce a grid of colorful dots inspired by the Hirst painting style. The color palette is dynamically generated from an image file (`spot_painting.jpg`).

---

## Customization

### Modify the Painting

- Adjust the number of dots and lines in `Painter.create_art()`:
  ```python
  painter.create_art(lines=15, dots_per_line=15)
  ```

- Change the dot size or spacing in the `Painter` constructor:
  ```python
  Painter(color_list=colors, dot_size=15, dot_spacing=40)
  ```

### Use a Different Color Palette

Replace the `spot_painting.jpg` file with your own image to create a new palette. Update the file path in `art_manager.py`:

```python
colors = self.color_palette.extract_colors("your_image.jpg", 30)
```

---

## Contributing

Feel free to fork the repository and submit pull requests with improvements or new features. Make sure to document your changes!

---

## License

Still working on it.

---

## Acknowledgments

- Inspired by Damien Hirst's iconic art style.
- Special thanks to the Python Turtle library for making graphics fun and accessible!

