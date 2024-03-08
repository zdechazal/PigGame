import unittest
import os
from Highscores import Highscore
from Human import Human


class TestHighscore(unittest.TestCase):
    def setUp(self):
        self.highscore = Highscore()

    def tearDown(self):
        os.remove(self.highscore.filepath)

    def test_add_player_to_list(self):
        player1 = Human("Bob")
        player2 = Human("Bob1")
        player1.highscore = 100
        player1.highscore = 200

        self.highscore.add_player_to_list(player1)
        self.assertIn(player1, self.highscore.all_player_list)

        self.highscore.add_player_to_list(player1)
        self.assertEqual(len(self.highscore.all_player_list), 1)

        self.highscore.add_player_to_list(player2)
        self.assertIn(player2, self.highscore.all_player_list)

    def test_save_and_load_scores(self):
        player1 = Human("Bob")
        player2 = Human("Bob1")
        player1.highscore = 100
        player2.highscore = 200

        self.highscore.add_player_to_list(player1)
        self.highscore.add_player_to_list(player2)

        self.highscore.save_scores()
        new_highscore = Highscore()
        new_highscore.load_scores()

        self.assertEqual(len(new_highscore.all_player_list), 2)
        self.assertIn(player1, new_highscore.all_player_list)
        self.assertIn(player2, new_highscore.all_player_list)

    def test_sort_scores(self):
        player1 = Human("Bob")
        player2 = Human("Bob1")
        player3 = Human("Bob2")
        player1.highscore = 100
        player2.highscore = 300
        player3.highscore = 200

        self.highscore.add_player_to_list(player1)
        self.highscore.add_player_to_list(player2)
        self.highscore.add_player_to_list(player3)

        self.highscore.sort_scores()

        self.assertEqual(self.highscore.top_ten[0], player1)
        self.assertEqual(self.highscore.top_ten[1], player3)
        self.assertEqual(self.highscore.top_ten[2], player2)


if __name__ == '__main__':
    unittest.main()
