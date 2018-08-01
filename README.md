# test-private-dependency

This is an empty python package meant only to help test that `pip` and `pipenv` are able to install requirements from private repositories using git+ssh. The point is that this package does not exist on `pypi`, and neither does a package with this name in order to exclude the chance of a false-positive.