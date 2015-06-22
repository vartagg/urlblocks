#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

version = '0.1'

setup(
    name='urlblocks',
    version=version,
    description='A utility class for manipulating URLs.',
    author_email="vartagg@users.noreply.github.com",
    url='http://github.com/vartagg/urlblocks',
    packages=find_packages(exclude=('test',)),
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
)
