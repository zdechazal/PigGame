from random import randint

class Turn:
    def __init__(self, player, winning_score):
        self.winning_score = winning_score
        self.player = player

    
    def roll_dice(self):
        return randint(1, 6)

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
            
            if self.is_one(roll_value): break #checks if the roll result is a 1, sets turn_total to 0 and breaks out of the loop          
            self.player.turn_total += roll_value
            print(f"{self.player.username}'s current turn total is {self.player.turn_total}")           
            
            if self.player.game_score + self.player.turn_total >= self.winning_score : break #checks if it has reached a winning score and breaks out of the loop
            
            keep_rolling = self.player.is_rolling() #asks the player roll/hold/quit and returns r/h/q

            if keep_rolling == "h": #breaks out of the loop and ends the turn allowing the return of the turn total
                break
            elif keep_rolling == "q": #returns -1 instead of the turn total and is then used in Game to break out of the loop/Game
                return -1

        return self.player.turn_total