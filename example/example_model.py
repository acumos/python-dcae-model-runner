#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# ===============LICENSE_START=======================================================
# Acumos Apache-2.0
# ===================================================================================
# Copyright (C) 2017-2018 AT&T Intellectual Property & Tech Mahindra. All rights reserved.
# ===================================================================================
# This Acumos software file is distributed by AT&T and Tech Mahindra
# under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# This file is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ===============LICENSE_END=========================================================
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
