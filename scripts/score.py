"""If the player win, this function calculates the player’s score""" 
def score(player_pv, potion_nbr):
    score_game = player_pv + (potion_nbr*50)
    return score_game