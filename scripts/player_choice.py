from player_attack import player_attack
from potion import potion 

player_choice = ("Attack", "Potion")
for i in player_choice:
    if i==0:
        player_attack()
    if i==1:
        potion()
