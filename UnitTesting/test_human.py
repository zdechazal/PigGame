import unittest
from PigGame.Human import Human
from unittest.mock import patch


class TestHuman(unittest.TestCase):
    def setUp(self):
        # Create a Player instance for testing
        self.username = "test_user"
        self.player = Human(self.username)

    def test_init(self):
        # Assert that the initial values are set correctly
        self.assertEqual(self.player.username, "test_user")
        self.assertEqual(self.player.turn_total, 0)
        self.assertEqual(self.player.game_score, 0)
        self.assertEqual(self.player.highscore, 0)
        self.assertEqual(self.player.number_of_turns, 0)

    def test_is_rolling(self):
        # Test when the decision is "r"
        with unittest.mock.patch('builtins.input', return_value='r'):
            result = self.player.is_rolling()
        self.assertEqual(result, "r")

        # Test when the decision is "h"
        with unittest.mock.patch('builtins.input', return_value='h'):
            result = self.player.is_rolling()
        self.assertEqual(result, "h")

        # Test when the decision is "q"
        with unittest.mock.patch('builtins.input', return_value='q'):
            result = self.player.is_rolling()
        self.assertEqual(result, "q")

if __name__ == '__main__':
    unittest.main()