"""HUMAN PLAYER CREATED AND MANAGED."""


class Human:
    """HUMAN CLASS FOR HUMAN PLAYERS."""

    def __init__(self, username):
        """HUMAN PLAYER CONSTRUCTOR."""
        self.username = username
        self.turn_total = 0
        self.game_score = 0
        self.highscore = 0
        self.number_of_turns = 0

    def is_rolling(self):
        """ROLL DECISION."""
        decision = input("Roll or hold? ")
        if decision == "r":
            return "r"
        elif decision == "h":
            print(f"{self.username} holds")
            return "h"
        elif decision == "q":
            return "q"
        else:
            print(
                """
            Invalid input! Enter:
            r to roll
            h to hold
            q to quit \n
            """
            )
            return self.is_rolling()

    def change_username(self, new_username):
        """USERNAME CHANGED."""
        self.username = new_username
