import random
from player_choice import choice

"""this function add a random pv number to the player but reduce the number by 1.  A error message display if he has no more potion."""
def use_potion(ppv, potion_nbr):
    potion = random.randint(15, 50)
    if potion_nbr>0:
        ppv += potion
        potion_nbr -= 1 
    else:
        print("Dommage tu n’as plus de potion")
        choice()

