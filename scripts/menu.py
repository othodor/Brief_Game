from player_choice import player_choice
from score_storage import score

"""This function displays a menu in which the player can navigate and start the game"""
def menu():
    choice = input("1. Oui aller au combat",
           "2. Voir les scores", "3. Quitter le jeu.")
    if choice == "1":
        player_choice()
    elif choice == "2":
        score()
    elif choice == "3":
        exit()

# Bonjour <name>, veux tu partir au combat ?
# 1. Oui aller au combat (-> lance le jeu)
# 2. Voir les scores (-> affiche les scores des joueurs précédents)
# 3. Quitter le jeu.
