from setuptools import setup, find_packages

setup(
    name='trustwallet-hooks',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'commitlint = commitlint.main:main',
        ],
    },
)