import random
from init_game import potion_init



def use_potion():
    potion = random(15, 50)
    if potion_nbr>0:
        player_pv += potion
        potion_nbr -= 1 
    else:
        print("Dommage tu n’as plus de potion")
        player_choice()

