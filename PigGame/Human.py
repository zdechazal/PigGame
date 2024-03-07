class Human:
    def __init__(self, username):
        self.username = username
        self.turn_total = 0
        self.game_score = 0
        self.games_played = 0
        self.games_won = 0

    def is_rolling(self):
        decision = input("Press r to roll or h to hold: ")
        if decision == "r":
            return "r"
        elif decision == "h":    
            print(f"{self.username} holds")
            return "h"
        elif decision == "q":
            return "q"
        else:
            print("Enter r or h!")

    def add_game(self):
        self.games_played += 1

    def add_win(self):
        self.games_won += 1

    def change_name(self,new_name):
        self.change_name = new_name