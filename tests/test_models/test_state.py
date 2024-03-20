#!/usr/bin/python3
"""Defines unit tests for the State class."""

from tests.test_models.test_base_model import test_basemodel
from models.state import State

class test_state(test_basemodel):
    """Test suite for the State class."""

    def __init__(self, *args, **kwargs):
        """Initializes test_state instance."""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """Test that the 'name' attribute of State instances is a string."""
        new = self.value()
        self.assertEqual(type(new.name), str)
