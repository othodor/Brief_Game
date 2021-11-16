import random
# from init_game import enemy_init

""" This function remove a random number of pv between 5,10 to the troll"""
def player_attack(epv):
    attack_player = random.randint(5, 10)
    epv = epv - attack_player
    # enemy_pv = enemy_init()
    # enemy_pv -= attack_player
    # print(enemy_pv)
    return epv
