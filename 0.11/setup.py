#!/usr/bin/env python

import os.path
from setuptools import setup

setup(
    name = 'TracTextileMacro',
    packages = ['Textile'],
    version = '0.11.0',

    author = 'Patrick Wagstrom',
    author_email = 'patrick@wagstrom.net',
    description = 'Implements Textile syntax WikiProcessor as a Trac macro.',
    long_description = open(os.path.join(os.path.dirname(__file__), 'README')).read(),
    keywords = '0.11 wagstrom processor macro wiki',
    url = 'http://trac-hacks.org/wiki/TextileMacro',
    license = 'BSD',

    entry_points = { 'trac.plugins': [ 'Textile.macro = Textile.macro' ] },
    classifiers = ['Framework :: Trac'],
    install_requires = ['Trac'],
)
