from Displays import Displays
from Game import Game
from Computer import Computer
from Computer import Computer
from Human import Human




def computer_mode_start(player_one):
    Displays.printBotMenu()

    difficultyLevel = input("Enter your choice (1 to 4): ")

    if difficultyLevel in {"1", "2", "3"}:
        player_two = Computer(difficultyLevel)
        pigGame = Game(player_one, player_two)  # starts a game with a username and difficulty lvl
        pigGame.start_game()

    elif difficultyLevel == "4":
        Displays.printMenu()

    else:
        print("Enter a valid choice")

def player_mode_start(player_one):
    
    player2_name = input("Enter the name of player two: ")
    player_two = Human(player2_name)

    pigGame = Game(player_one, player_two)
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
    
    
    player1_name = input("\nEnter the name of player one: ")
    player_one = Human(player1_name)

    while True:
        Displays.printMenu()
        choice = input("Enter your choice (1 to 5): ")

        match choice:
            case "1":
                computer_mode_start(player_one)

            case "2":
                player_mode_start(player_one)

            case "3":
                pass #HighScore.displayScores(playerName)

            case "4":
                print(player_one.games_played)
            case "5":
                Displays.printRules()

            case "6":
                exit()
            case default:
                print("Enter a valid")


if __name__ == '__main__':
    main()