import sys
import os

# Add the parent directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                '..')))


import unittest
from color_palette import ColorPalette


class TestColorPalette(unittest.TestCase):
    def setUp(self):
        self.palette = ColorPalette()

    def test_is_too_light(self):
        """Test the _is_too_light method"""
        from collections import namedtuple
        RGB = namedtuple('RGB', ['r', 'g', 'b'])

        # Should return True for near-white colors
        self.assertTrue(self.palette._is_too_light(RGB(251, 251, 251)))

        # Should return False for colored values
        self.assertFalse(self.palette._is_too_light(RGB(200, 100, 100)))


if __name__ == '__main__':
    unittest.main()
