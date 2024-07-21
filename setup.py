# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='log-parser',
    version='0.1.0',
    description='code for springborard mini project',
    long_description=readme,
    author='Mithlesh Pandey',
    author_email='mithlesh.pandey@gmail.com',
    url='',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

