import pytest
import os
import sys
import inspect
import mock
import module 
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

from menu import menu
    
def test_menu():
    with mock.patch.object(__builtins__, 'input', lambda: 'some_input'):
        assert module.menu() == 'expected_output'

# L’ input doit être égal à 1, 2 ou 3

# Sinon un message d’erreur doit être renvoyer