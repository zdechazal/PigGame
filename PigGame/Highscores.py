"""PLAYER STATISTICS MANAGED."""

import pickle
from PigGame import Human


class Highscore:
    """LISTS AND UPDATES MANAGED."""

    def __init__(self, normal_mode):
        """HIGHSCORES CONSTRUCTOR."""
        self.all_player_list = list()
        self.top_ten = []
        if normal_mode:
            self.filepath = "players_highscores.pkl"
        else:
            self.filepath = "players_highscores_cheat.pkl"
        # different highscore list for cheat mode
        self.load_scores()

    # adds player to the list if it's not already
    def add_player_to_list(self, player: Human.Human):
        """PLAYER ADDED TO LIST."""
        if player not in self.all_player_list:
            self.all_player_list.append(player)

    # saves all players
    def save_scores(self):
        """HIGHSCORES SAVED TO FILE."""
        with open(self.filepath, "wb") as playerFile:
            pickle.dump(self.all_player_list, playerFile)

    # loads player to list, if empty EOF exception makes empty list
    def load_scores(self):
        """HIGHCORES LOADED INTO LIST."""
        try:
            with open(self.filepath, "rb") as playerFile:
                self.all_player_list = pickle.load(playerFile)
        except FileNotFoundError:
            print(f"File not found: {self.filepath}. ")
            return []
        except EOFError:
            self.all_player_list = list()

    # used to parse top 10 scores if list is not empty
    def sort_scores(self):
        """HIGHSCORES SORTED."""
        if self.all_player_list:
            sorted(self.all_player_list, key=lambda x: x.highscore)
            self.top_ten = self.all_player_list[0:10]

    # used to print scores
    def display_scores(self):
        """HIGHSCORES DISPAYED."""
        self.sort_scores()
        print("\n│ - - - - - - - - - - - - - - -│")
        print("│          Highscores          │")
        print("│ - - - - - - - - - - - - - - -│")
        print("|                              |")
        for player in self.top_ten:
            print(f"|  {player.username:20}  {player.highscore:^5} |")
        print("│ - - - - - - - - - - - - - - -│")
