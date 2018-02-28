# -*- coding: utf-8 -*-
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
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: Apache Software License',
    ],
    dependency_links=[
        'git+https://gerrit.onap.org/r/dcaegen2/utils.git#egg=dcaeapplib-0.0.4&subdirectory=dcaeapplib'
    ],
    description='Provides an Acumos model runner for DCAE',
    entry_points={
        'console_scripts': [
            'acumos_dcae_model_runner=acumos_dcae_model_runner.runner:run_model'
        ]
    },
    install_requires=[
        'acumos>=0.5.0',
        'dcaeapplib==0.0.4'  # pinned temporarily until package matures
    ],
    keywords='acumos dcae',
    license='Apache License 2.0',
    long_description='\n'.join(_long_descr()),
    name='acumos_dcae_model_runner',
    packages=find_packages(),
    python_requires='>=3.4',
    url='https://gerrit.acumos.org/r/gitweb?p=python-dcae-model-runner.git',
    version='0.1.0',
)
