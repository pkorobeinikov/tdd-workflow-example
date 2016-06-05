# -*- coding: utf-8 -*-

import unittest

from ddt import ddt, unpack, data

from calculation import Summator, Subtractor, Multiplier, Divider, Calculator


@ddt
class SummatorTestCase(unittest.TestCase):
    @unpack
    @data({'expected': 4, 'given': {'a': 1, 'b': 3}})
    def testSum(self, expected, given):
        actual = Summator().sum(given['a'], given['b'])
        self.assertEqual(expected, actual)


@ddt
class SubtractorTestCase(unittest.TestCase):
    @unpack
    @data({'expected': 2, 'given': {'a': 3, 'b': 1}})
    def testSub(self, expected, given):
        actual = Subtractor().sub(given['a'], given['b'])
        self.assertEqual(expected, actual)


@ddt
class MultiplierTestCase(unittest.TestCase):
    @unpack
    @data({'expected': 6, 'given': {'a': 3, 'b': 2}})
    def testMul(self, expected, given):
        actual = Multiplier().mul(given['a'], given['b'])
        self.assertEqual(expected, actual)


@ddt
class DividerTestCase(unittest.TestCase):
    # Arrange
    def setUp(self): self.sut = Divider()

    @unpack
    @data({'expected': 2, 'given': {'a': 4, 'b': 2}})
    def testDiv(self, expected, given):
        # Act
        actual = self.sut.div(given['a'], given['b'])

        # Assert
        self.assertEqual(expected, actual)

    def testDivByZero(self):
        # Act and Assert
        with self.assertRaises(ZeroDivisionError):
            self.sut.div(1, 0)


@ddt
class CalculatorComplexTestCase(unittest.TestCase):
    # Arrange
    def setUp(self):
        self.sut = Calculator(Summator(),
                              Subtractor(),
                              Multiplier(),
                              Divider())

    @unpack
    @data({'expected': 4, 'given': {'a': 1, 'b': 3}})
    def testSum(self, expected, given):
        # Act
        actual = self.sut.sum(given['a'], given['b'])

        # Assert
        self.assertEqual(expected, actual)

    @unpack
    @data({'expected': 2, 'given': {'a': 3, 'b': 1}})
    def testSub(self, expected, given):
        # Act
        actual = self.sut.sub(given['a'], given['b'])

        # Assert
        self.assertEqual(expected, actual)

    @unpack
    @data({'expected': 6, 'given': {'a': 3, 'b': 2}})
    def testMul(self, expected, given):
        # Act
        actual = self.sut.mul(given['a'], given['b'])

        # Assert
        self.assertEqual(expected, actual)

    @unpack
    @data({'expected': 2, 'given': {'a': 4, 'b': 2}})
    def testDiv(self, expected, given):
        # Act
        actual = self.sut.div(given['a'], given['b'])

        # Assert
        self.assertEqual(expected, actual)

    def testDivByZero(self):
        # Act and Assert
        with self.assertRaises(ZeroDivisionError):
            self.sut.div(1, 0)
