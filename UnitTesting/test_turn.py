import unittest
from unittest.mock import MagicMock
from PigGame.Turn import Turn


class TestTurn(unittest.TestCase):
    def setUp(self):
        self.player = MagicMock()
        self.player.game_score = 0
        self.player.turn_total = 0
        self.winning_score = 100
        self.turn = Turn(self.player, self.winning_score)

    def test_roll_dice(self):
        for _ in range(100):
            roll_value = self.turn.roll_dice()
            self.assertTrue(1 <= roll_value <= 6)

    def test_is_one(self):
        self.assertTrue(self.turn.is_one(1))
        self.assertFalse(self.turn.is_one(2))
        self.assertFalse(self.turn.is_one(3))
        self.assertFalse(self.turn.is_one(4))
        self.assertFalse(self.turn.is_one(5))
        self.assertFalse(self.turn.is_one(6))

    def test_play_turn_quit(self):
        # Mocking player's is_rolling method to return 'q' to simulate quitting
        self.player.is_rolling.return_value = "q"
        self.assertEqual(self.turn.play_turn(), -1)  # Player quits, return -1

    def test_play_turn_rolls_one(self):
        # Mocking player's is_rolling method to return 'r' every time, but the roll is always 1
        self.player.is_rolling.return_value = "r"
        self.turn.roll_dice = MagicMock(return_value=1)
        self.assertEqual(
            self.turn.play_turn(), 0
        )  # Player rolls a 1, turn total becomes 0


if __name__ == "__main__":
    unittest.main()
