from setuptools import (
    find_packages,
    setup,
)

setup(
    name='test-private-dependency',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    long_description='just for testing dependency links work',
    dependency_links=[],
    install_requires=['requests']
)
