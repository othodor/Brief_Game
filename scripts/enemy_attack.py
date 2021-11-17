import random


""" This function remove a random number of pv between 5 and 15 to the player. """

def enemy_attack(ppv):
    attack_enemy = random.randint(5, 15)
    ppv = ppv - attack_enemy
    return ppv

