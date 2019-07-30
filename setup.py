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
from os.path import dirname, abspath, join as path_join
from setuptools import setup, find_packages


SETUP_DIR = abspath(dirname(__file__))
DOCS_DIR = path_join(SETUP_DIR, 'docs')


def _long_descr():
    '''Yields the content of documentation files for the long description'''
    for file in ('README.rst', 'tutorial/index.rst', 'release-notes.rst', 'contributing.rst'):
        doc_path = path_join(DOCS_DIR, file)
        with open(doc_path) as f:
            yield f.read()


setup(
    author='Paul Triantafyllou',
    author_email='trianta@research.att.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: Apache Software License',
    ],
    description='Provides an Acumos model runner for DCAE',
    entry_points={
        'console_scripts': [
            'acumos_dcae_model_runner=acumos_dcae_model_runner.runner:run_model'
        ]
    },
    install_requires=[
        'acumos>=0.5.0',
        'dcaeapplib<2.0.0'
    ],
    keywords='acumos dcae',
    license='Apache License 2.0',
    long_description='\n'.join(_long_descr()),
    name='acumos_dcae_model_runner',
    packages=find_packages(),
    python_requires='>=3.5',
    url='https://gerrit.acumos.org/r/gitweb?p=python-dcae-model-runner.git',
    version='0.1.3',
)
