def welcome():
    """ This function ask for a pseudoname"""
    player_name = input("Bienvenue dans ce Brief Game. Quel est votre pseudo?")
    print(f'Bonjour {player_name}, veux tu partir au combat ?')
    return player_name
    