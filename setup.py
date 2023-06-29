from setuptools import setup
import sys,os

setup(
    name = 'signalgen',
    version = '1.0.0',
    description = 'System time based signal generator for stdin-to-modbus-shm',
    license='MIT',
    author = 'Nikolas Koesling',
    packages = ['src'],
    package_data={},
    install_requires=['future'],
    entry_points = {
        'console_scripts': [
            'signalgen=src.signalgen:main']
            },
    classifiers = ['Operating System :: OS Independent',
            'Programming Language :: Python :: 3.6',
            'Operating System :: MacOS :: MacOS X',
            'Operating System :: Microsoft :: Windows',
            'Operating System :: POSIX',
            'License :: MIT'],
)
