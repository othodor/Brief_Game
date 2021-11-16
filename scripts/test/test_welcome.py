import pytest
import os
import sys
import inspect
# import mock

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

from welcome import welcome  

def test_welcome():
    assert welcome('John Do') == 'Bonjour John Do, veux tu partir au combat ?'
# def test_welcome(monkeypatch):
#     monkeypatch.setattr('builtins.welcome', lambda x : "Mark")
#     assert welcome() == 'Bonjour Mark, veux tu partir au combat ?'   