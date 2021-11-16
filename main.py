from scripts import menu, display, enemy_attack, init_game, play_again, player_attack, player_choice, potion, pv_check, score_storage, score, welcome

"""Welcoming message, and first input asking for player name and if he's ready to play"""
welcome.welcome()

player_name = welcome.welcome().player_name


"""Display menu and ask the player to make a choice"""
menu.menu()

"""Display player, enemy and potion infos"""
display.display_info()


""""Variables"""
player_pv = init_game.player_init()
enemy_pv = init_game.enemy_init()
potion_nbr = init_game.potion_init()
pv_check = pv_check.pv_check()


"""Display Menu"""
menu.menu()

"""While Loop until the player or the enemy have no more PV"""
while pv_check==True:
    player_choice.choice()
    enemy_attack.enemy_attack(player_pv)

"""Calculating the final score"""
score.score()

"""Score storage"""
score_storage.score_storage()


""""Play again"""
play_again.play_again()