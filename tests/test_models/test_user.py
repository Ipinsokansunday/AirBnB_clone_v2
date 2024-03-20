#!/usr/bin/python3
"""Defines unit tests for the User class."""

from tests.test_models.test_base_model import test_basemodel
from models.user import User

class test_User(test_basemodel):
    """Test suite for the User class."""

    def __init__(self, *args, **kwargs):
        """Initializes test_User instance."""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """Test that the 'first_name' attribute of User instances is a string."""
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """Test that the 'last_name' attribute of User instances is a string."""
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """Test that the 'email' attribute of User instances is a string."""
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """Test that the 'password' attribute of User instances is a string."""
        new = self.value()
        self.assertEqual(type(new.password), str)
