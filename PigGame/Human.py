class Human:
    def __init__(self, username):
        self.username = username
        self.turn_total = 0
        self.game_score = 0

    def is_rolling(self):
        decision = input("Press r to roll or h to hold: ")
        if decision == "r":
            return True
        elif decision == "h":    
            print(f"{self.username} holds")
            return False
        else:
            print("Enter r or h!")