import unittest
import pickle
from PigGame.Highscores import Highscore
from PigGame.Human import Human


class TestHighscore(unittest.TestCase):

    def test_add_player_to_list(self):
        self.highscore = Highscore(True)
        h1 = Human("bob")
        h1.highscore = 4
        self.highscore.add_player_to_list(h1)
        self.assertIn(h1, self.highscore.all_player_list)

    def test_save_scores(self):
        self.highscore = Highscore(True)
        self.highscore.all_player_list = list()
        h1 = Human("bob")
        h1.highscore = 4

        self.highscore.all_player_list.append(h1)
        self.highscore.save_scores()

        # Read saved data from the file
        with open(self.highscore.filepath, "rb") as playerFile:
            saved_data = pickle.load(playerFile)

        self.assertEqual(
            saved_data[0].highscore, self.highscore.all_player_list[0].highscore
        )

    def test_load_scores(self):
        self.highscore = Highscore(True)
        self.highscore.all_player_list = list()
        h1 = Human("bob")
        h1.highscore = 4
        self.highscore.all_player_list.append(h1)
        self.highscore.save_scores()

        self.highscore.load_scores()

        self.assertEqual(self.highscore.all_player_list[0].highscore, 4)

    def test_sort_scores(self):
        self.highscore = Highscore(True)
        self.highscore.all_player_list = list()
        h1 = Human("bob")
        h1.highscore = 4
        h2 = Human("bob2")
        h2.highscore = 4
        players = []
        players.append(h1)
        players.append(h2)
        self.highscore.all_player_list.extend(players)
        self.highscore.sort_scores()

        expected_top_ten = sorted(players, key=lambda x: x.highscore, reverse=True)[:10]
        self.assertEqual(self.highscore.top_ten, expected_top_ten)


if __name__ == "__main__":
    unittest.main()
