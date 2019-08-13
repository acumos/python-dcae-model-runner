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
'''
Provides tests for the structure of the project
'''
from os.path import dirname, abspath, join as path_join
from xml.etree import ElementTree

import acumos_dcae_model_runner


SETUP_DIR = abspath(dirname(dirname(__file__)))


def test_version_match():
    '''Asserts that the library version matches pom.xml'''
    pom_path = path_join(SETUP_DIR, 'pom.xml')
    root = ElementTree.parse(pom_path).getroot()
    version = root[3]
    assert version.text == acumos_dcae_model_runner.__version__
