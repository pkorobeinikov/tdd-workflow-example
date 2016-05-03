# -*- coding: utf-8 -*-

import unittest
from ddt import ddt, data, unpack
from app import greeter


@ddt
class GreeterTestCase(unittest.TestCase):
    @unpack
    @data({'expected': 'Hello, World!', 'given': 'World'},
          {'expected': 'Hello, Tests!', 'given': 'Tests'})
    def test_greet(self, expected, given):
        actual = greeter.greet(given)
        self.assertEqual(expected, actual)

    def test_loud_greet(self):
        actual = greeter.loud_greet('')
        self.assertEqual('HI!', actual)
