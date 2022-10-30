#!/usr/bin/env python3
"""Test nodule for the base_model class"""


import unittest
from unittest.mock import patch
from models.base_model import BaseModel


class test_base_model__init(unittest.TestCase):
    """A test class for the base_model class"""

    @patch('BaseModel')
    def test_id_type(self):
        testInstance = BaseModel()
        self.assertTrue(isinstance(testInstance.id, str))

    def test_id_unique(self):
        pass

    def test_created_at(self):
        pass

    def test_updated_at(self):
        pass
