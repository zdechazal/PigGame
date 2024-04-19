"""COMPUTER OPPONENT CREATED AND MANAGED."""

import time


class Computer:
    """COMPUTER CLASS FOR AI PLAYER."""

    def __init__(self, difficulty):
        """AI PLAYER CONSTRUCTOR."""
        self.username = "Bob the AI"
        self.difficulty = difficulty
        self.turn_total = 0
        self.game_score = 0
        self.number_of_turns = 0
        self.highscore = 0

    def is_rolling(self):
        """CONDITIONS FOR COMPUTER ROLL SET."""
        match self.difficulty:
            case "1":  # Easy level
                return self.decision_logic(40)
            # From wikipedia, gives an 8% disadvantage:
            case "2":  # Medium level
                return self.decision_logic(25)
            # From wikipedia, gives a 4% disadvantage:
            case "3":  # Hard level
                return self.decision_logic(20)

    def decision_logic(self, turn_max):
        """CONDITIONS CHECKED."""
        time.sleep(1)
        return True if self.turn_total < turn_max else False
