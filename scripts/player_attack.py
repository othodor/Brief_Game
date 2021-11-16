import random

""" This function remove a random number of pv between 5 and 10 to the troll"""
def player_attack(epv):
    attack_player = random.randint(5, 10)
    epv = epv - attack_player
    return epv
