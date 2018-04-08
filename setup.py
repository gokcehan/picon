from setuptools import setup

setup(
    name='picon',
    version='1',
    description='Run your code in python interactive console from the command line',
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
