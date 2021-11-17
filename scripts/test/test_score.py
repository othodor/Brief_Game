import pytest
import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 


from score import score

def test_score():
    assert score(28, 1) == 78
    assert score(20, 0) == 20
    assert score(18, 2) == 118