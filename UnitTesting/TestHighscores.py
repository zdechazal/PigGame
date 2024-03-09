import unittest
from unittest.mock import MagicMock
from TestFolder.Highscores import Highscore

class TestHighscores(unittest.TestCase):
    def setUp(self):
        self.highscores = Highscore()

    def test_add_player_to_list(self):
        player1 = MagicMock()
        player2 = MagicMock()
        self.highscores.add_player_to_list(player1)
        self.assertIn(player1, self.highscores.all_player_list)
        self.highscores.add_player_to_list(player2)
        self.assertIn(player2, self.highscores.all_player_list)

    def test_save_scores(self):
        player1 = MagicMock()
        player2 = MagicMock()
        self.highscores.all_player_list = [player1, player2]
        with unittest.mock.patch("pickle.dump") as mock_dump:
            self.highscores.save_scores()
            mock_dump.assert_called_once_with([player1, player2], unittest.mock.ANY)

    def test_load_scores(self):
        with unittest.mock.patch("pickle.load") as mock_load:
            self.highscores.load_scores()
            mock_load.assert_called_once_with(unittest.mock.ANY)

    def test_sort_scores(self):
        player1 = MagicMock(highscore=5)
        player2 = MagicMock(highscore=10)
        player3 = MagicMock(highscore=15)
        self.highscores.all_player_list = [player1, player2, player3]
        self.highscores.sort_scores()
        self.assertEqual(self.highscores.top_ten, [player1, player2, player3])

    def test_display_scores(self):
        with unittest.mock.patch("builtins.print") as mock_print:
            player1 = MagicMock(username="Alice", highscore=5)
            player2 = MagicMock(username="Bob", highscore=10)
            player3 = MagicMock(username="Charlie", highscore=15)
            self.highscores.top_ten = [player1, player2, player3]
            self.highscores.display_scores()
            mock_print.assert_any_call("Highscores:")
            mock_print.assert_any_call("Alice, 5")
            mock_print.assert_any_call("Bob, 10")
            mock_print.assert_any_call("Charlie, 15")

if __name__ == '__main__':
    unittest.main()