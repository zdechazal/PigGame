from Turn import Turn
class Game:
    def __init__(self, player_one, player_two):
        self.player_one = player_one
        self.player_two = player_two


    def start_game(self):
        player = self.player_one
        while True:
            turn = Turn(player)
            player.game_score += turn.play_turn()
            print(f"{player.username} has {player.game_score} total points")
            if self.hasWon(player) == True:
                break
            player = self.switch_player(player)
            

    def switch_player(self, player):
        if player == self.player_one:
            return self.player_two
        elif self.player_two:
            return self.player_one

    @staticmethod
    def hasWon(player):
        if player.game_score > 15:
           print(f"\n{player.username} has won!!!")
           return True
        return False
    

    