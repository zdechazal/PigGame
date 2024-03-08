import pickle

class Highscore:
    def __init__(self):
        self.all_player_list = []
        self.top_ten = []
        self.filepath = "players_highscores.pkl"

        with open(self.filepath, "a"):  # ensures file exists
            pass

        # Added this so if the list is not empty, it loads. Must be loaded once only, at the very beginning.
        self.load_scores()


    def add_player_to_list(self, player):  # adds player to the list if it's not already
        if player not in self.all_player_list:
            self.all_player_list.append(player)


    def save_scores(self): # saves all players
        with open(self.filepath, "wb") as playerFile:
            pickle.dump(self.all_player_list, playerFile)


    def load_scores(self):  # loads player to list, if empty EOF exception makes empty list
        try:
            with open(self.filepath, "rb") as playerFile:
                self.all_player_list = pickle.load(playerFile)

        except FileNotFoundError:
            print(f"File not found: {self.filepath}. ")
            return []

        except EOFError:
            self.all_player_list = []


    def sort_scores(self):  # used to parse top 10 scores
        if self.all_player_list:  # if list is not empty
            self.all_player_list.sort(key=lambda player: player.number_of_turns, reverse=True)
            self.top_ten = self.all_player_list[0:10]


    def display_scores(self):  # used to print scores
        self.sort_scores()
        print("Highscores:")
        for player in self.top_ten:
            print(f"{player.username}, {player.number_of_turns}")

