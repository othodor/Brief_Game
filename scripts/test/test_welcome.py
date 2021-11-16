import pytest
import os
import sys
import inspect

import mock
import module

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

from welcome import welcome  

def test_welcome():
    with mock.patch.object(__builtins__, 'input', lambda: 'some_input'):
        assert module.welcome() == 'expected_output'
    