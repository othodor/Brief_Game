from player_attack import player_attack
from enemy_attack import ennemy_attack



""" this function check if the game is over"""
def pv_check():
    enemy_pv = player_attack()
    player_pv = ennemy_attack()
    if enemy_pv <= 0:
        print("Partie gagnée.")
        return False
    elif player_pv <= 0:
        print("Partie perdue.")
        return False
    else:
        return True