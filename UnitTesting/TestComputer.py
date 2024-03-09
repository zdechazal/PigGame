import unittest
from unittest.mock import patch
from PigGame.Computer import Computer


class TestComputer(unittest.TestCase):
    def setUp(self):
        self.computer = Computer("1")
        self.easy = Computer("1")
        self.medium = Computer("2")
        self.hard = Computer("3")

    def test_is_rolling_easy(self):
        with patch('builtins.input', side_effect=['n']):
            self.easy.turn_total = 10
            self.assertTrue(self.easy.is_rolling())

            self.easy.turn_total = 25
            self.assertFalse(self.easy.is_rolling())

    def test_is_rolling_medium(self):
        with patch('builtins.input', side_effect=['n']):
            self.medium.turn_total = 20
            self.assertTrue(self.medium.is_rolling())

            self.medium.turn_total = 30
            self.assertFalse(self.medium.is_rolling())

    def test_is_rolling_hard(self):
        with patch('builtins.input', side_effect=['n']):
            self.hard.turn_total = 10
            self.assertTrue(self.hard.is_rolling())

            self.hard.turn_total = 20
            self.assertFalse(self.hard.is_rolling())

    def test_decision_logic_below_max(self):
        # Test when turn_total is below turn_max
        self.computer.turn_total = 10
        self.assertTrue(self.computer.decision_logic(20))

    def test_decision_logic_above_max(self):
        # Test when turn_total is above turn_max
        self.computer.turn_total = 25
        self.assertFalse(self.computer.decision_logic(20))


if __name__ == '__main__':
    unittest.main()
