"""
Turn class: Class for each separate turn per game, has dice in it for rolling.

Logic for each turn is in this class.
"""

from random import randint


class Turn:
    """LOGIC FOR EACH TURN IMPLEMENTED."""

    def __init__(self, player, winning_score):
        """TURN CONSTRUCTOR."""
        self.winning_score = winning_score
        self.player = player

    def roll_dice(self):
        """DICE ROLLED."""
        return randint(1, 6)

    def is_one(self, roll_value):
        """IF ONE ROLLED RETURN TRUE."""
        if roll_value == 1:
            self.player.turn_total = 0
            return True
        return False

    def play_turn(self):
        """LOGIC IMPLEMENTED."""
        print(f"\n{self.player.username}'s turn to play")
        self.player.turn_total = 0
        keep_rolling = True
        while keep_rolling:
            roll_value = self.roll_dice()
            print(f"\n{self.player.username} rolls a {roll_value}")

            if self.is_one(roll_value):
                break
            self.player.turn_total += roll_value
            print(
                f"{self.player.username}'s current turn "
                + "total is {self.player.turn_total}"
            )
            # checks if it has reached a winning score
            # and breaks out of the loop
            if self.player.game_score + self.player.turn_total >= self.winning_score:
                break
            # asks the player roll/hold/quit and returns r/h/q
            keep_rolling = self.player.is_rolling()
            # breaks out of the loop and ends
            # the turn allowing the return of the turn total
            if keep_rolling == "h":
                break
            # returns -1 instead of the turn totaL
            # and used in Game to break out of the loop/Game
            elif keep_rolling == "q":
                self.player.turn_total = -1
                break

        return self.player.turn_total
