import time


class Computer:
    def __init__(self, difficulty):
        self.username = "Bob the AI"
        self.difficulty = difficulty
        self.turn_total = 0
        self.game_score = 0
        self.number_of_turns = 0
        self.highscore = 0

    def is_rolling(self):
        match self.difficulty:
            case "1":  # Easy level
                return self.decision_logic(
                    20
                )  # From wikipedia, gives an 8% disadvantage
            case "2":  # Medium level
                return self.decision_logic(25)  # From wikipedia, those are all
            case "3":  # Hard level
                return self.decision_logic(15)  # To be tweaked still

    def decision_logic(self, turn_max):
        time.sleep(1)
        return True if self.turn_total < turn_max else False
