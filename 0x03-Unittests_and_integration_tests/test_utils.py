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
            [{"a": 1}, ("a",), 1],
            [{"a": {"b": 2}}, ("a",), {"b": 2}],
            [{"a": {"b": 2}}, ("a", "b"), 2],
    ])
    def test_access_nested_map(self, nested_map, path, res):
        """ test cases
        """
        self.assertEqual(access_nested_map(nested_map, path), res)
