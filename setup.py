# Copyright 2023, Herve Yav.

from setuptools import setup, find_packages


setup(
    name="cinemax",
    version="0.1",
    description="Purchase a ticket to watch a movie as a user then a PDF receipt will be generated.",
    author="Herve Yav",
    author_email="rvyav@hotmail.com",
    url="https://github.com/rvyav/python-cinemax",
    install_requires=[],
    tests_require=["pytest"],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
