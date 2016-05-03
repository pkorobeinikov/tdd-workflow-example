# -*- coding: utf-8 -*-


def greet(name):
    if not name:
        return 'Hi!'
    return 'Hello, {name}!'.format(name=name)


def loud_greet(name):
    return greet(name).upper()
