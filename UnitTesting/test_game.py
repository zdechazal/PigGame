import unittest
from unittest.mock import MagicMock
from PigGame.Game import Game
from PigGame import Human
from PigGame.Computer import Computer
from PigGame.Highscores import Highscore


class TestGame(unittest.TestCase):
    def setUp(self):
        self.player_one = Human.Human("Alice")
        self.player_two = Computer(1)
        self.highscores_main = Highscore(True)
        self.game = Game(self.player_one, self.player_two, True, self.highscores_main)

    def test_switch_player(self):
        self.assertIs(self.game.switch_player(self.player_one), self.player_two)
        self.assertIs(self.game.switch_player(self.player_two), self.player_one)

    def test_has_won(self):
        self.assertFalse(self.game.has_won(self.player_one))
        self.assertFalse(self.game.has_won(self.player_two))
        self.player_one.game_score = 100
        self.assertTrue(self.game.has_won(self.player_one))

    def test_check_if_player_highscore(self):
        self.player_one.number_of_turns = 10
        self.game.check_if_player_highscore(self.player_one)
        self.assertEqual(self.player_one.highscore, 10)
        self.player_one.highscore = 20
        self.game.check_if_player_highscore(self.player_one)
        self.assertEqual(self.player_one.highscore, 20)

    def test_reset_game_score(self):
        self.player_one.game_score = 30
        self.player_two.number_of_turns = 5
        self.game.reset_game_score()
        self.assertEqual(self.player_one.game_score, 0)
        self.assertEqual(self.player_two.game_score, 0)
        self.assertEqual(self.player_one.number_of_turns, 0)
        self.assertEqual(self.player_two.number_of_turns, 0)


if __name__ == "__main__":
    unittest.main()
