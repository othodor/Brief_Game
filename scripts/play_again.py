from init_game import player_init, enemy_init, potion_init
from menu import menu


"""this function restart the game if the player wants to"""
def play_again():
    
    print("Partie terminée. Veux-tu jouer une autre partie?")
    player_response = input()
    if player_response == "Yes":
        player_init()
        enemy_init()
        potion_init()
            
    elif player_response == "No":
        menu()
    else:
        print("Error, try again!")
