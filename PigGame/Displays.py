"""
Display class: Most of the print statements are stored in display
"""


class Displays:

    @staticmethod
    def printRules():
        rules = """
        │ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - |
        |                                                 Rules                                                           |
        │ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - | 
        |                                                                                                                 |
        | Each turn, a player repeatedly rolls a die until either a 1 is rolled or the player decides to "hold":          |
        |                                                                                                                 |
        | If the player rolls a 1, they score nothing and it becomes the next player's turn.                              |
        | If the player rolls any other number, it is added to their turn total and the player's turn continues.          |
        | If a player chooses to "hold", their turn total is added to their score, and it becomes the next player's turn. |
        |                                                                                                                 |
        | The first player to score 100 or more points wins.   (Wikipedia)                                                           |
        |                                                                                                                 |
        | Cheat mode allows the first player to score 30 to win.                                                          |
        |                                                                                                                 |
        | To roll press r                                                                                                 |
        | To hold press h                                                                                                 |
        | To exit mid game, press q                                                                                       |
        │ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - |
            """
        print(rules)

    @staticmethod
    def printMenu():
        main_menu = """
        │ - - - - - - - - - - - - - - - │
        │           Pig Game            │
        │ - - - - - - - - - - - - - - - │
        │ 1. Play versus bot            │
        │ 2. Play with another player   │
        │ 3. Show highscores            |
        | 4. Change username            │
        │ 5. Rules                      │
        │ 6. Quit                       │
        │ - - - - - - - - - - - - - - - │

        """
        print(main_menu)

    @staticmethod
    def printBotMenu():
        bot_menu = """
        │ - - - - - - - - - - - - - │
        │     Select Difficulty     │
        │ - - - - - - - - - - - - - │
        │ 1. Easy                   │
        │ 2. Medium                 │
        │ 3. Hard                   |
        | 4. Back                   │
        │ - - - - - - - - - - - - - │

        """
        print(bot_menu)

    @staticmethod
    def printPlayerOptions():
        player_menu = """
        │ - - - - - - - - - - - - - │
        │     Player Options        │
        │ - - - - - - - - - - - - - │
        │ 1. Previous scores        │
        │ 2. Change name            │
        | 3. Back                   │
        │ - - - - - - - - - - - - - │"""
        print(player_menu)

    @staticmethod
    def printHighscoreHeader():
        print("\n│ - - - - - - - - - - - - - - -│")
        print("│          Highscores          │")
        print("│ - - - - - - - - - - - - - - -│")
        print("|                              |")
