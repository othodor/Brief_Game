import pytest
import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 


from ennemy_attack import ennemy_attack

def test_ennemy_attack():
    assert ennemy_attack() ==