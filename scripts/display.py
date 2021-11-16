from player_attack import enemy_pv
from enemy_attack import player_pv
from potion import potion_nbr


def display_info():
    print(f"Il vous reste {player_pv} points de vie et {potion_nbr} potions, l'ennemi a {enemy_pv}")