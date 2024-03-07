from Turn import Turn
from Human import Human
from Computer import Computer

class Game:
    def __init__(self, player_one, player_two):
        self.player_one = player_one
        self.player_two = player_two


    def start_game(self):
        player = self.player_one
        while True:
            turn = Turn(player)
            turn_result = turn.play_turn()
            if turn_result == -1:
                self.reset_game_score()
                break
            player.game_score += turn_result
            print(f"{player.username} has {player.game_score} total points")
            if self.has_won(player) == True:
                self.add_user_stats(player)
                self.reset_game_score()
                break
            player = self.switch_player(player)
        
        
            

    def switch_player(self, player):
        if player == self.player_one:
            return self.player_two
        elif self.player_two:
            return self.player_one

    
    def has_won(self, player):
        if player.game_score >= 15:
           print(f"\n{player.username} has won!!!")
           return True
        return False
    
    def add_user_stats(self, player):

        if player == self.player_one and self.player_two is Human:
            self.player_one.games_won += 1
            self.player_one.games_played += 1
            self.player_two.games_played += 1
        elif player == self.player_one and self.player_two is Computer:
            self.player_one.games_won += 1
            self.player_one.games_played += 1
        elif player == self.player_two and player is Human:
            self.player_two.games_won += 1
            self.player_two.games_played += 1
            self.player_one.games_played += 1
        elif player == self.player_two and player is Computer:
            self.player_one.games_played += 1

    def reset_game_score(self):
        self.player_one.game_score = 0
        self.player_two.game_score = 0

        
    
    

    