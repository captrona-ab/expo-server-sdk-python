from setuptools import find_packages
from setuptools import setup
import os
import re


HERE = os.path.abspath(os.path.dirname(__file__))


README_PATH = os.path.join(HERE, 'README.md')
try:
    with open(README_PATH) as fd:
        README = fd.read()
except IOError:
    README = ''


# This is a forked repository.
# Please view the original at https://github.com/expo/exponent-server-sdk-python.
setup(
    name='exponent_server_sdk',
    version='0.3.1',
    description='Expo Server SDK for Python',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/captrona-ab/expo-server-sdk-python',
    author='Expo Team and Kraftkallan Team',
    author_email='drift-kontroll@hemoskola.se',
    license='MIT',
    install_requires=[
        'requests',
        'six',
    ],
    packages=find_packages(),
    zip_safe=False
)
