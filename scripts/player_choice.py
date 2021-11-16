from player_attack import player_attack
from potion import use_potion 

def choice():
    player_choices = ("Attack", "Potion")
    print(player_choices)
    player_choice = input()
    if player_choice=="Attack":
        player_attack()
    if player_choice=="Potion":
        use_potion()
