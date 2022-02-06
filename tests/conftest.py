import pytest
import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) # python to look a level up 
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from SDLC import app

@pytest.fixture
def app_test():
    app_test = app
    return app_test
