#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
"""
Creates an example Acumos model for DCAE on-boarding testing
"""
from acumos.modeling import Model, NamedTuple
from acumos.session import AcumosSession


class NumbersIn(NamedTuple):
    x: int
    y: int


class NumberOut(NamedTuple):
    result: int


def add(numbers: NumbersIn) -> NumberOut:
    '''Adds two integers'''
    x, y = numbers
    return NumberOut(x + y)


model = Model(add=add)

session = AcumosSession()
session.dump(model, 'example-model', '.')
