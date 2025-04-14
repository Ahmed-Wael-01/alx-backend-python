#!/usr/bin/env python3
""" test utils
"""
import unittest
from utils import access_nested_map
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """ suite of tests for utils
    """
    @parameterized.expand([
            ["first", {"a": 1}, ("a",), 1],
            ["second", {"a": {"b": 2}}, ("a",), {"b": 2}],
            ["third", {"a": {"b": 2}}, ("a", "b"), 2],
    ])
    def test_access_nested_map(self, name, nested_map, path, res):
        """ test access
        """
        self.assertEqual(access_nested_map(nested_map, path), res)
