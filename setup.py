#!/usr/bin/env python

from setuptools import setup

version = '1.0.0'

required = open('requirements.txt').read().split('\n')

setup(
    name='y',
    version=version,
    description='Quality control of sanger sequencing reads',
    author='olgabot',
    author_email='olga.botvinnik@gmail.com',
    url='https://github.com/czbiohub/winky',
    packages=['winky'],
    install_requires=required,
    long_description='See ' + 'https://github.com/czbiohub/winky',
    license='MIT'
)
