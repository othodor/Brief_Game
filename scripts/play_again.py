from init_game import 
from menu import menu
again = ("Yes", "No")
print("Partie terminée. Veux-tu jouer une autre partie?")
def play_again():
    player_response = input()
    for i in again:
        if player_response == "Yes":
            init_game()
            menu()
        if player_response == "No":
            exit()


