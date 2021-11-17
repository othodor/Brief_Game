def score(player_pv, potion_nbr):
    """If the player win, this function calculates the player’s score""" 
    score_game = player_pv + (potion_nbr*50)
    return score_game