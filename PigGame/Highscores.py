import pickle


class Highscore:
    def __init__(self, normal_mode):
        self.all_player_list = []
        self.top_ten = []
        # different highscore list for cheat mode
        if normal_mode == True:
            self.filepath = "players_highscores.pkl"
        else:
            self.filepath = "players_highscores_cheat.pkl"
        with open(self.filepath, "a"):
            pass
        self.load_scores()

    # adds player to the list if it's not already
    def add_player_to_list(self, player):
        if player not in self.all_player_list:
            self.all_player_list.append(player)

    # saves all players
    def save_scores(self):
        with open(self.filepath, "wb") as playerFile:
            pickle.dump(self.all_player_list, playerFile)

    # loads player to list, if empty EOF exception makes empty list
    def load_scores(self):
        try:
            with open(self.filepath, "rb") as playerFile:
                self.all_player_list = pickle.load(playerFile)
        except FileNotFoundError:
            print(f"File not found: {self.filepath}. ")
            return []
        except EOFError:
            self.all_player_list = []

    # used to parse top 10 scores if list is not empty
    def sort_scores(self):
        if self.all_player_list:
            self.all_player_list.sort(key=lambda player: player.highscore)
            self.top_ten = self.all_player_list[0:10]

    # used to print scores
    def display_scores(self):
        self.sort_scores()
        print("\n│ - - - - - - - - - - - - - - -│")
        print("│          Highscores          │")
        print("│ - - - - - - - - - - - - - - -│")
        print("|                              |")
        for player in self.top_ten:
            print(f"|  {player.username:20}  {player.highscore:^5} |")
        print("│ - - - - - - - - - - - - - - -│")
