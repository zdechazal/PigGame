import unittest
from unittest.mock import MagicMock
from Game import Game

class TestGame(unittest.TestCase):

    def setUp(self):
        self.player_one = MagicMock()
        self.player_two = MagicMock()
        self.highscores_main = MagicMock()

    def test_switch_player(self):
        game = Game(self.player_one, self.player_two, True, self.highscores_main)
        self.assertEqual(game.switch_player(self.player_one), self.player_two)
        self.assertEqual(game.switch_player(self.player_two), self.player_one)

    def test_has_won(self):
        game = Game(self.player_one, self.player_two, True, self.highscores_main)
        self.player_one.game_score = 20
        self.assertFalse(game.has_won(self.player_one))
        self.player_one.game_score = 40
        self.assertTrue(game.has_won(self.player_one))

    def test_check_if_player_highscore(self):
        game = Game(self.player_one, self.player_two, True, self.highscores_main)
        self.player_one.number_of_turns = 10
        game.check_if_player_highscore(self.player_one)
        self.assertEqual(self.player_one.highscore, 10)
        self.player_one.number_of_turns = 5
        game.check_if_player_highscore(self.player_one)
        self.assertEqual(self.player_one.highscore, 10)


if __name__ == '__main__':
    unittest.main()
