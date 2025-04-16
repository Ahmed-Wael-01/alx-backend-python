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

    @patch('requests.get')
    def test_get_json(self, mock_get):
        """ tests expected results
        """
        mock_response = Mock()
        res = [{"payload": True}, {"payload": False}]
        urls = ["http://example.com", "http://holberton.io"]
        for i in range(2):
            mock_response.json.return_value = res[i]
            mock_get.return_value = mock_response
            payload = get_json(urls[i])
            mock_get.assert_called_with(urls[i])
            self.assertEqual(payload, res[i])
