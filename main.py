import sys
sys.path.append('scripts')

import welcome, display, enemy_attack, init_game, score_storage, score, potion, player_attack

""""Variables"""
player_pv = init_game.player_pv
enemy_pv = init_game.enemy_pv
potion_nbr = init_game.potion_nbr

"""Welcoming message, and first input asking for player name and if he's ready to play"""
player_name = welcome.welcome()

"""Display menu and ask the player to make a choice"""
def menu():
    player_choice = input("1. Oui aller au combat \n2. Voir les scores \n3. Quitter le jeu.")
    if player_choice == "1":
        return True
    elif player_choice == "2":
        with open("save.txt") as save:
            print(save.read())
            return save.read()
    elif player_choice == "3":
        exit()
    else:
        print("Huuh?")
menu = menu()


"""this fonction init player's turn he can choose between attack or drink a potion"""
def choice(menu, pnbr, ppv, epv, name):
    display.display_info(name, ppv, pnbr, epv)
    if menu == True:
        player_choice = input("1. Attaquer \n2.Boire une potion \nTape 1 ou 2")
        while player_choice not in ["1", "2"]:
            print("Mauvaise réponse!")
            player_choice = input("1. Attaquer \n2.Boire une potion \nTape 1 ou 2")
        if player_choice == "1":
            epv = player_attack.player_attack(epv)
        elif player_choice == "2":
            if pnbr > 0:
                ppv = potion.use_potion(ppv)
                pnbr -= 1
            else:
                print("Dommage tu n’as plus de potion")
    """"Troll turn"""
    ppv = enemy_attack.enemy_attack(ppv)
    return pnbr, ppv, epv


"""While Loop until the player or the enemy have no more PV"""
def pv_check(epv, ppv):
    if epv <= 0:
        print("Partie gagnée.")
        return False
    elif ppv <= 0:
        print("Partie perdue.")
        return False
    else:
        return True
            
while pv_check(enemy_pv, player_pv) == True: 
    potion_nbr, player_pv, enemy_pv = choice(menu, potion_nbr, player_pv, enemy_pv, player_name)

"""Calculating the final score"""
score = score.score(player_pv, potion_nbr)
print(score)

"""Score storage"""
score_storage.score_storage(player_name, score)

