from enemy_attack import player_pv
from potion import potion_nbr

def score():
    score_game = player_pv + (potion_nbr*50)
    return score_game