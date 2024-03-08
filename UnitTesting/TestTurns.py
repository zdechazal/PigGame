import unittest
from unittest.mock import patch
from Human import Human
from Turn import Turn

class TestTurn(unittest.TestCase):
    def setUp(self):
        self.player = Human("Bob")
        self.winning_score = 100
        self.turn = Turn(self.player, self.winning_score)

    @patch("turn_module.randint", return_value=3)  # Mocking randint to always return 3
    def test_roll_dice(self, mock_randint):
        self.assertEqual(self.turn.roll_dice(), 3)

    def test_is_one(self):
        self.player.turn_total = 0
        self.assertTrue(self.turn.is_one(1))
        self.assertEqual(self.player.turn_total, 0)

        self.player.turn_total = 10
        self.assertFalse(self.turn.is_one(3))
        self.assertEqual(self.player.turn_total, 10)

    @patch("builtins.input", side_effect=["h"])  # Mocking user input to hold
    def test_play_turn_hold(self, mock_input):
        self.player.game_score = 50
        self.player.turn_total = 20
        self.assertEqual(self.turn.play_turn(), 20)

    @patch("builtins.input", side_effect=["r", "r", "h"])  # Mocking user input to roll, roll, hold
    @patch("turn_module.randint", side_effect=[3, 4, 1])  # Mocking dice rolls to return 3, 4, 1
    def test_play_turn_roll_hold(self, mock_randint, mock_input):
        self.player.game_score = 50
        self.assertEqual(self.turn.play_turn(), 8)  # 3 + 4 + 1 = 8

    @patch("builtins.input", side_effect=["q"])  # Mocking user input to quit
    def test_play_turn_quit(self, mock_input):
        self.assertEqual(self.turn.play_turn(), -1)

if __name__ == "__main__":
    unittest.main()
