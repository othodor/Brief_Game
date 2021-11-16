from player_choice import player_choice
from score_storage import score

choices = {"1. Oui aller au combat",
           "2. Voir les scores", "3. Quitter le jeu."}
print(choices)


def menu(l):
    choice = input()
    for l in choices:
        if choice == "1":
            player_choice()
        if choice == "2":
            score()
        if choice == "3":
            exit()


# Bonjour <name>, veux tu partir au combat ?
# 1. Oui aller au combat (-> lance le jeu)
# 2. Voir les scores (-> affiche les scores des joueurs précédents)
# 3. Quitter le jeu.
