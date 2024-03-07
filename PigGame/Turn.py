from random import randint

class Turn:
    def __init__(self, player):
        self.player = player

    
    def roll_dice(self):
        return randint(1, 6)  # Adjusted to 6-sided dice

    def is_one(self, roll_value):
        if roll_value == 1:
            self.player.turn_total = 0
            return True
        return False


    def play_turn(self):
        
        print(f"\n{self.player.username}'s turn to play")
        self.player.turn_total = 0
        keep_rolling = True
        while keep_rolling:
            roll_value = self.roll_dice()

            print(f"\n{self.player.username} rolls a {roll_value}")
            if self.is_one(roll_value): break  # Breaks loop if is_one returns True

            
            
            self.player.turn_total += roll_value
            print(f"{self.player.username}'s current turn total is {self.player.turn_total}")           
            if self.player.game_score + self.player.turn_total >= 15 : break
            keep_rolling = self.player.is_rolling()

            if keep_rolling == "h": 
                break
            elif keep_rolling == "q":
                return -1

        return self.player.turn_total