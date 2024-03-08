from Turn import Turn
from Human import Human
from Computer import Computer
from Highscores import Highscore

class Game:
    def __init__(self, player_one, player_two, normal_mode, highscores_main):
        self.player_one = player_one
        self.player_two = player_two
        self.highscores_main = highscores_main
        if normal_mode == True:
            self.winning_score = 40
        else:
            self.winning_score = 15


    def start_game(self):
        player = self.player_one
        while True:
            turn = Turn(player, self.winning_score) 
            turn_result = turn.play_turn() #starts a player's turn
            if turn_result == -1: #player quit the game
                self.reset_game_score()
                break
            player.number_of_turns += 1
            player.game_score += turn_result
            print(f"{player.username} has {player.game_score} total points")
            if self.has_won(player) == True:
                self.check_if_player_highscore(player)
                self.highscores_main.add_player_to_list(player)
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

    
    def check_if_player_highscore(self, player):
        if player.highscore < player.number_of_turns:
            player.highscore = player.number_of_turns


    def reset_game_score(self):
        self.player_one.game_score = 0
        self.player_two.game_score = 0
        self.player_one.number_of_turns = 0
        self.player_two.number_of_turns = 0
