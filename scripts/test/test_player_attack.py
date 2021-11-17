import pytest
import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 


from player_attack import player_attack

def test_player_attack():
	""" this function tests if the attack of the player is between 5 and 10 and if this argments must be integers and different of 0."""
    assert 30<=player_attack(45)<=40
    assert 25<=player_attack(40)<=35
    with pytest.raises(TypeError):
        player_attack("a",0,5.5)