import pytest
import os
import sys
import inspect
import mock
import module

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

from play_again import play_again  

def test_play_again():
    with mock.patch.object(__builtins__, 'input', lambda: 'some_input'):
        assert module.play_again() == 'expected_output'