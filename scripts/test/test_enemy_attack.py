import pytest
import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 


from enemy_attack import enemy_attack

def test_ennemy_attack():
    assert 30<=enemy_attack(45)<=40
    assert 25<=enemy_attack(40)<=35
    with pytest.raises(TypeError):
        enemy_attack("a",0,5.5)