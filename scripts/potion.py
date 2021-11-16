import random
# from init_game import potion_init, player_init
import player_choice


def use_potion(ppv, potion_nbr):
    potion = random.randint(15, 50)
    # potion_nbr = potion_init()
    # player_pv = player_init()
    if potion_nbr>0:
        ppv += potion
        potion_nbr -= 1 
    else:
        print("Dommage tu n’as plus de potion")
        player_choice()

