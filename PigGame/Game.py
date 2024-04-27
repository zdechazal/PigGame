"""GAME STARTPOINT."""

from PigGame.Turn import Turn


class Game:
    """GAME INSTANCE CREATED."""

    def __init__(self, player_one, player_two, normal_mode, highscores_main):
        """GAME CONSTRUCTOR."""
        self.player_one = player_one
        self.player_two = player_two
        self.highscores_main = highscores_main
        if normal_mode:
            self.winning_score = 100
        else:
            self.winning_score = 30

    def start_game(self):
        """GAME STARTED."""
        player = self.player_one
        while True:
            # starts a new player's turn to roll
            turn = Turn(player, self.winning_score)
            # starts a player's turn
            turn_result = turn.play_turn()
            # player quits the game when play_turn returns -1
            if turn_result == -1:
                self.reset_game_score()
                break
            player.number_of_turns += 1
            player.game_score += turn_result
            print(f"{player.username} has {player.game_score} total points")
            # if player won, it checks if this turn is a highscore for player
            # adds the player object to the persistent highscore list
            if self.has_won(player):
                self.check_if_player_highscore(player)
                self.highscores_main.add_player_to_list(player)
                self.reset_game_score()
                break
            player = self.switch_player(player)

    def switch_player(self, player):
        """PLAYERS SWITCHED."""
        if player == self.player_one:
            return self.player_two
        elif self.player_two:
            return self.player_one

    def has_won(self, player):
        """GAME WIN DECIDED."""
        if player.game_score >= self.winning_score:
            print(f"\n{player.username} has won!!!")
            return True
        return False

    def check_if_player_highscore(self, player):
        """HIGHSCORE UPDATE."""
        if player.highscore < player.number_of_turns:
            player.highscore = player.number_of_turns

    def reset_game_score(self):
        """GAME RESET."""
        self.player_one.game_score = 0
        self.player_two.game_score = 0
        self.player_one.number_of_turns = 0
        self.player_two.number_of_turns = 0
