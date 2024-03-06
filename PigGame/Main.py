from Displays import Displays
from Game import Game
from Computer import Computer
from Computer import Computer
from Human import Human




def computer_mode_start():
    print()
    Displays.printBotMenu()

    difficultyLevel = input("Enter your choice (1 to 4): ")
    player1Name = input("\nEnter the name of player one: ")
    playerOne = Human(player1Name)

    if difficultyLevel in {"1", "2", "3"}:
        playerTwo = Computer(difficultyLevel)
        pigGame = Game(playerOne, playerTwo)  # starts a game with a username and difficulty lvl
        pigGame.start_game()

    elif difficultyLevel == "4":
        Displays.printMenu()

    else:
        print("Enter a valid choice")

def player_mode_start():
    player1Name = input("\nEnter the name of player one: ")
    player2Name = input("Enter the name of player two: ")
    playerOne = Human(player1Name)
    playerTwo = Human(player2Name)

    pigGame = Game(playerOne, playerTwo)
    pigGame.start_game()

def user_options():
    pass

    '''Displays.printPlayerOptions()
    option = input("\nEnter your choice (1 to 3): ")

    match option:
        case "1":
            pass

        case "2":
            newUsername = input("What's the new username: ")
            playerOne.changeUsername(newUsername)'''
    
def main():

    while True:
        Displays.printMenu()
        choice = input("Enter your choice (1 to 5): ")

        match choice:
            case "1":
                computer_mode_start()

            case "2":
                player_mode_start()

            case "3":
                pass #HighScore.displayScores(playerName)

            case "4":
                user_options()

            case "5":
                Displays.printRules()

            case "6":
                break

            case default:
                print("Enter a valid")


if __name__ == '__main__':
    main()