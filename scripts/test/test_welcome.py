import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

from welcome import welcome  

def test_welcome(monkeypatch):
	"""this function tests the input of the main menu"""
    monkeypatch.setattr('builtins.input', lambda x : "Mark")
    assert welcome() == 'Bonjour Mark, veux tu partir au combat ?'   