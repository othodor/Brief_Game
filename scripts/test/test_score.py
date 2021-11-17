import pytest
import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 


from score import score

def test_score():
	"""this function tests the calculation of the score if the player win the game. The score must be equal to the sum of the number of life points of the player and the number of potions mutiply for 50."""
    assert score(28, 1) == 78
    assert score(20, 0) == 20
    assert score(18, 2) == 118