#!/usr/bin/env python3

from distutils.core import setup

setup(name='python-yr',
      version='1.2.2-dev',
      description='Get the forecast from the norwegian wheather service yr.no in python',
      author='wckd @ github, idxxx23 @ github',
      author_email='alexander.l.hansen@gmail.com',
      url='https://github.com/wckd/python-yr',
      packages=['yr'],
      package_data={'yr': ['languages/*.json']},
      install_requires=['requests', 'xmltodict', 'beautifulsoup4'],
     )
