import random
# from init_game import player_init

""" This function remove a random number of pv between 5 and 15 to the player. """

def ennemy_attack(ppv):
    attack_enemy = random.randint(5, 15)
    ppv = ppv - attack_enemy
    # player_pv = player_init()
    # player_pv -= attack_enemy
    return ppv

