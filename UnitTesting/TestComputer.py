import unittest
from unittest.mock import patch
from Computer import Computer

class TestComputer(unittest.TestCase):
    def setUp(self):
        self.computer_easy = Computer("1")
        self.computer_medium = Computer("2")
        self.computer_hard = Computer("3")

    def test_is_rolling_easy(self):
        with patch('builtins.input', side_effect=['n']):
            self.computer_easy.turn_total = 10
            self.assertTrue(self.computer_easy.is_rolling())

            self.computer_easy.turn_total = 25
            self.assertFalse(self.computer_easy.is_rolling())

    def test_is_rolling_medium(self):
        with patch('builtins.input', side_effect=['n']):
            self.computer_medium.turn_total = 20
            self.assertTrue(self.computer_medium.is_rolling())

            self.computer_medium.turn_total = 30
            self.assertFalse(self.computer_medium.is_rolling())

    def test_is_rolling_hard(self):
        with patch('builtins.input', side_effect=['n']):
            self.computer_hard.turn_total = 10
            self.assertTrue(self.computer_hard.is_rolling())

            self.computer_hard.turn_total = 20
            self.assertFalse(self.computer_hard.is_rolling())

if __name__ == '__main__':
    unittest.main()
