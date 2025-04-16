#!/usr/bin/env python3
""" test utils
"""
import unittest
from utils import access_nested_map, get_json
from parameterized import parameterized
from unittest.mock import patch, Mock


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

    @parameterized.expand([
            [{}, ("a",), 'a'],
            [{"a": 1}, ("a", "b"), 'b']
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """ tests exceptions
        """
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)
        self.assertEqual("KeyError('{}')".format(expected), repr(e.exception))


class TestGetJson(unittest.TestCase):
    """ test get_json
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """ Test that utils.get_json returns the expected result."""
        config = {'return_value.json.return_value': test_payload}
        patcher = patch('requests.get', **config)
        mock = patcher.start()
        self.assertEqual(get_json(test_url), test_payload)
        mock.assert_called_once()
        patcher.stop()
