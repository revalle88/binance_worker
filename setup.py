from setuptools import find_packages, setup


name = 'binance'
version = '1.0.0'

setup(
    name=name,
    version=version,
    packages=find_packages(),
    package_dir={'': 'src'},
    install_requires=[],
)
