import unittest
from unittest.mock import patch
from Game import Game
from Human import Human
from Highscores import Highscore

class TestGame(unittest.TestCase):
    def setUp(self):
        self.player_one = Human("Bob")
        self.player_two = Human("Bob1")
        self.highscores_main = Highscore()

    @patch("game_module.Turn.play_turn", return_value=20)  # Mocking Turn.play_turn to return 20
    def test_start_game_player_one_wins(self, mock_play_turn):
        game = Game(self.player_one, self.player_two, normal_mode=True, highscores_main=self.highscores_main)
        game.start_game()
        self.assertEqual(self.player_one.game_score, 20)
        self.assertEqual(self.player_one.number_of_turns, 1)
        self.assertTrue(game.has_won(self.player_one))

    @patch("game_module.Turn.play_turn", side_effect=[20, -1])  # Mocking Turn.play_turn to return 20 and then quit
    def test_start_game_player_one_quits(self, mock_play_turn):
        game = Game(self.player_one, self.player_two, normal_mode=True, highscores_main=self.highscores_main)
        game.start_game()
        self.assertEqual(self.player_one.game_score, 0)
        self.assertEqual(self.player_one.number_of_turns, 1)
        self.assertFalse(game.has_won(self.player_one))
        self.assertTrue(game.has_won(self.player_two))

    @patch("game_module.Turn.play_turn", return_value=20)  # Mocking Turn.play_turn to return 20
    def test_switch_player(self, mock_play_turn):
        game = Game(self.player_one, self.player_two, normal_mode=True, highscores_main=self.highscores_main)
        self.assertEqual(game.switch_player(self.player_one), self.player_two)
        self.assertEqual(game.switch_player(self.player_two), self.player_one)

    def test_has_won(self):
        game = Game(self.player_one, self.player_two, normal_mode=True, highscores_main=self.highscores_main)
        self.player_one.game_score = 50
        self.assertTrue(game.has_won(self.player_one))
        self.assertFalse(game.has_won(self.player_two))

    def test_check_if_player_highscore(self):
        game = Game(self.player_one, self.player_two, normal_mode=True, highscores_main=self.highscores_main)
        self.player_one.number_of_turns = 20
        game.check_if_player_highscore(self.player_one)
        self.assertEqual(self.player_one.highscore, 20)

    def test_reset_game_score(self):
        game = Game(self.player_one, self.player_two, normal_mode=True, highscores_main=self.highscores_main)
        self.player_one.game_score = 50
        self.player_two.number_of_turns = 20
        game.reset_game_score()
        self.assertEqual(self.player_one.game_score, 0)
        self.assertEqual(self.player_two.game_score, 0)
        self.assertEqual(self.player_one.number_of_turns, 0)
        self.assertEqual(self.player_two.number_of_turns, 0)

if __name__ == "__main__":
    unittest.main()
