# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='py-ethscan',
    version='0.0.1',
    description='Python Ethereum Blockchain Explorer',
    long_description=readme,
    author='Christoph Mussenbrock',
    author_email='blockchain@mussenbrock.de',
    url='https://github.com/christoph2806/py-ethscan',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

