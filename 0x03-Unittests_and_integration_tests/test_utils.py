#!/usr/bin/env python3
""" test for the utils.access_nested_map function"""

import utils
import Typing
from unittest import unittest.TestCase
nested_map = utils.access_nested_map

@parameterized.expand([
    ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
class TestAccessNestedMap(unittest.TestCase):
    TestAccessNestedMap.test_access_nested_map(nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)



