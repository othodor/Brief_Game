import pytest
import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

from display import display_info  

def test_display():
    assert display_info("Mark", 28, 1, 14) == "Mark, il vous reste 28 points de vie et 1 potion(s), l'ennemi a 14"
