from welcome import player_name
from score import score

score_game=score()
with open("save.txt", "a") as save:
    for i in save:
        save.write('\n'.join(player_name, score_game))
