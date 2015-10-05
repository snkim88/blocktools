# -*- coding: utf-8 -*-
from distutils.core import setup

setup(
    name='blocktools',
    version='0.1.1',
    author="Hendrik 'Bloody' Schumann, Alex Gorale",
    author_email='pypi@schumann.pw',
    packages=['blocktools'],
    scripts=['bin/sight.py'],
    url='https://github.com/Nyancoins/blocktools',
    license='BSD3',
    description='Bitcoin blockchain parser',
    long_description=open('README.md').read(),
)