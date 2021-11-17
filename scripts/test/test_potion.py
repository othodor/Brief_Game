import pytest
import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 


from potion import use_potion

def test_potion():
    assert 40<=use_potion(25)<=50
    assert 27<=use_potion(12)<=50 
    assert 17<=use_potion(2)<=50