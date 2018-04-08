from setuptools import setup, find_packages

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='picon',
    version='1.0.0',
    description='Run your code in python interactive console from the command line',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/gokcehan/picon',
    author='Gokcehan Kara',
    author_email='gokcehankara@gmail.com',
    packages=['picon'],
    entry_points={
        'console_scripts': [
            'picon=picon:main',
        ],
    },
)
