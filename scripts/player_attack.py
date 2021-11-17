import random

def player_attack(epv):
	""" This function remove a random number of pv between 5 and 10 to the troll"""
    attack_player = random.randint(5, 10)
    epv = epv - attack_player
    return epv
