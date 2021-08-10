#!/usr/bin/env python
# Encoding: utf-8
#  _____.__           .
# /  _____/           |\
# | |_|_|.__ _._  ..  | |.  ._ .____
# |  __/|/ _` | \ /\ /| | | | / ___/
# | | | | (.] |\ V  V | | \.| \___ \
# | | | |\__,_/.\_/\_/| |\__  [____/
# |/   \|             |/ \___/
# '     '             '
__author__ = 'Jacob Betz'
__email__ = 'jake@baruek.net'
__version__ = '0.0.1'


from setuptools import setup, find_packages


setup(
    name='flawlys',
    version=__version__,
    url='https://github.com/euheimr/flawlys',
    license='BSD-3',
    author=__author__,
    author_email=__email__,
    packages=find_packages(),
    description='A Dockerized Analytics Dashboard for Qualys and Amazon Web Services.',
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: BSD-3 License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',
    install_requires=[
        'flask',
        'boto3',
        'boto3_extensions',
        'requests',
        'dash',
        'plotly',
        'pandas',
    ],

)
