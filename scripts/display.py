"""This function print informations about the player's pv( and the number of potions he has ) and the monster's pv."""
def display_info(player_name, player_pv, potion_nbr, enemy_pv):
    print(f"{player_name}, il vous reste {player_pv} points de vie et {potion_nbr} potion(s), l'ennemi a {enemy_pv}")