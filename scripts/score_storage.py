def score_storage(player_name, score):
    """ this function add and store in a txt file, the player's name and his score"""
    with open("save.txt", "a") as save:
        save.write('\n' + player_name + " " + str(score))
