from Turn import Turn
from Human import Human
from Computer import Computer

class Game:
    def __init__(self, player_one, player_two, normal_mode = True):
        self.player_one = player_one
        self.player_two = player_two
        if normal_mode == True:
            self.winning_score = 40
        else:
            self.winning_score = 10


    def start_game(self):
        player = self.player_one
        while True:
            turn = Turn(player, self.winning_score) 
            turn_result = turn.play_turn() #starts a player's turn
            if turn_result == -1: #player quit the game
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
        if player.game_score >= self.winning_score:
           print(f"\n{player.username} has won!!!")
           return True
        return False
    
    def add_user_stats(self, player): #this could be simplified by giving the computer the games_won and games_played attributes
        if player == self.player_one:
            self.player_one.games_won += 1
            self.player_one.games_played += 1
            self.player_two.games_played += 1
        elif player == self.player_two:
            self.player_two.games_won += 1
            self.player_two.games_played += 1
            self.player_one.games_played += 1

        '''if player == self.player_one and isinstance(self.player_two,Human):
            self.player_one.games_won += 1
            self.player_one.games_played += 1
            self.player_two.games_played += 1
        elif player == self.player_one and isinstance(self.player_two, Computer):
            self.player_one.games_won += 1
            self.player_one.games_played += 1
        elif player == self.player_two and isinstance(player ,Human):
            self.player_two.games_won += 1
            self.player_two.games_played += 1
            self.player_one.games_played += 1
        elif player == self.player_two and isinstance(player ,Computer):
            self.player_one.games_played += 1'''

    def reset_game_score(self):
        self.player_one.game_score = 0
        self.player_two.game_score = 0
        self.player_one.number_of_turns = 0
        self.player_two.number_of_turns = 0
