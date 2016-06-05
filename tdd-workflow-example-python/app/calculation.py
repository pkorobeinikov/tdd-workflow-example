# -*- coding: utf-8 -*-

class Summator(object):
    def sum(self, a, b): return a + b


class Subtractor(object):
    def sub(self, a, b): return a - b


class Multiplier(object):
    def mul(self, a, b): return a * b


class Divider(object):
    def div(self, a, b): return a / b


class Calculator(object):
    def __init__(self, summator, subtractor, multiplier, divider):
        self.summator = summator
        self.subtractor = subtractor
        self.multiplier = multiplier
        self.divider = divider

    def sum(self, a, b): return self.summator.sum(a, b)

    def sub(self, a, b): return self.subtractor.sub(a, b)

    def mul(self, a, b): return self.multiplier.mul(a, b)

    def div(self, a, b): return self.divider.div(a, b)
