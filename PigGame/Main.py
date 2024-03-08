from Displays import Displays
from Game import Game
from Computer import Computer
from Computer import Computer
from Human import Human
from Highscores import Highscore


def computer_mode_start(player_one, is_normal_mode, highscores_main):
    Displays.printBotMenu()

    difficultyLevel = input("Enter your choice (1 to 4): ")

    if difficultyLevel in {"1", "2", "3"}:
        player_two = Computer(difficultyLevel)
        pigGame = Game(
            player_one, player_two, is_normal_mode, highscores_main
        )  # starts a game with a username and difficulty lvl
        pigGame.start_game()

    elif difficultyLevel == "4":
        Displays.printMenu()

    else:
        print("Enter a valid choice")


def player_mode_start(player_one, is_normal_mode, highscores_main):

    player2_name = input("Enter the name of player two: ")
    player2_name = check_name(player2_name)
    player_two = Human(player2_name)

    pigGame = Game(player_one, player_two, is_normal_mode, highscores_main)
    pigGame.start_game()


def get_play_mode():
    while True:
        user_input = input("Test using cheat mode? (y/n): ")
        if user_input == "n":
            return True
        elif user_input == "y":
            return False
        else:
            print("Incorrect input")

def check_name(name):
    if not name.isalnum():
        return check_name(input("\nOnly letters and number allowed!"
                         + "Enter the name again: \n"))
    else: return name
        




def main():

    is_normal_mode = get_play_mode()  #
    player1_name = input("\nEnter the name of player one: ")
    player1_name = check_name(player1_name)
    player_one = Human(player1_name)
    highscores_main = Highscore()

    while True:
        Displays.printMenu()
        choice = input("Enter your choice (1 to 5): ")

        match choice:
            case "1":
                computer_mode_start(player_one, is_normal_mode, highscores_main)

            case "2":
                player_mode_start(player_one, is_normal_mode, highscores_main)

            case "3":
                highscores_main.display_scores()

            case "4":
                new_username = input("\nNew username: ")
                new_username = check_name(new_username)
                player_one.change_username(new_username)
            case "5":
                Displays.printRules()
            case "6":
                highscores_main.save_scores()
                exit()
            case default:
                print("Enter a valid choice!")


if __name__ == "__main__":
    main()
