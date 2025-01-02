import sys
import os

# Add the parent directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                '..')))


import unittest
from painter import Painter
from turtle import Screen


class TestPainter(unittest.TestCase):
    def setUp(self):
        self.test_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
        self.painter = Painter(self.test_colors)

    def test_initialization(self):
        """Test painter initialization"""
        self.assertEqual(self.painter.color_list, self.test_colors)
        self.assertEqual(self.painter.dot_size, 20)
        self.assertEqual(self.painter.spacing, 50)

    def tearDown(self):
        Screen().bye()


if __name__ == '__main__':
    unittest.main()
