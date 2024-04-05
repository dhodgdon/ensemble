# AI assisted in the creation of this code.

from setuptools import setup, find_packages

setup(
    name='ensemble',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'ensemble=ensemble.cli:main',
        ],
    },
    install_requires=[
        'music21',
        'sly'
    ],
    author='Dallin Hodgdon',
    author_email='dhodgdon7@gmail.com',
    description='Ensemble Language - The musical programming language',
    url='https://github.com/dhodgdon/ensemble',
    license='MIT',
)
