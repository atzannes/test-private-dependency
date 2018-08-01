import os
from setuptools import (
    find_packages,
    setup,
)

VERSION = '0.1'

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='test-private-dependency',
    version=VERSION,
    packages=find_packages(),
    include_package_data=True,
    long_description=README,
    dependency_links=[],
    install_requires=['requests']
)
