from welcome import player_name
from score import score

""" this function add and store in a txt file, the player's name and his score"""
def score_storage():
    score_game=score()
    with open("save.txt", "a") as save:
        save.write('\n'.join(player_name, score_game))
