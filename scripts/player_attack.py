import random

""" This function reduce a random number of pv between 5 and 10 of the troll"""
def player_attack(epv):
    attack_player = random.randint(5, 10)
    epv = epv - attack_player
    return epv
