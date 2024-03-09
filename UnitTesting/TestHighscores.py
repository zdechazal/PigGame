import unittest
import pickle
from PigGame.Highscores import Highscore
from PigGame.Human import Human


class TestHighscore(unittest.TestCase):
    def setUp(self):
        self.highscore = Highscore()

    def tearDown(self):
        self.highscore = None

    def test_add_player_to_list(self):
        player = {"username": "TestPlayer", "highscore": 4}
        self.highscore.add_player_to_list(player)
        self.assertIn(player, self.highscore.all_player_list)

    def test_save_scores(self):
        player = {"username": "Bob", "highscore": 4}
        self.highscore.all_player_list.append(player)
        self.highscore.save_scores()

        # Read saved data from the file
        with open(self.highscore.filepath, "rb") as playerFile:
            saved_data = pickle.load(playerFile)

        self.assertEqual(saved_data, self.highscore.all_player_list)

    def test_load_scores(self):
        player = {"username": "Bob", "highscore": 4}
        self.highscore.all_player_list.append(player)
        self.highscore.save_scores()

        self.highscore.load_scores()

        self.assertEqual(self.highscore.all_player_list, [player])

    def test_sort_scores(self):
        players = [{"username": "Bob", "highscore": 4}, {"username": "Bob2", "highscore": 4}]
        self.highscore.all_player_list.extend(players)
        self.highscore.sort_scores()

        expected_top_ten = sorted(players, key=lambda x: x["highscore"], reverse=True)[:10]
        self.assertEqual(self.highscore.top_ten, expected_top_ten)


if __name__ == '__main__':
    unittest.main()