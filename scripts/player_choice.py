from player_attack import player_attack
from potion import use_potion 


"""this fonction init player's turn he can choose between attack or drink a potion"""
def choice():
    player_choice = input("1. Attaquer \n2.Boire une potion \nTape 1 ou 2")
    while player_choice!=1 or player_choice!=2:
        print("Choix incorrecte!")
        player_choice = input("1. Attaquer \n2.Boire une potion \nTape 1 ou 2")
        if player_choice=="Attack":
            player_attack()
        elif player_choice=="Potion":
            use_potion()