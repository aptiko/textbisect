#!/usr/bin/env python3

from setuptools import setup, find_packages


setup(
    name="textbisect",
    version="DEV",
    license="GPL3",
    description="Binary search in a sorted text file",
    author="Antonis Christofides",
    author_email="antonis@antonischristofides.com",
    url="https://github.com/openmeteo/textbisect",
    packages=find_packages(),
    test_suite="tests",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        ("License :: OSI Approved :: GNU General Public License "
         "v3 or later (GPLv3+)"),
        "Topic :: Text Processing :: Indexing",
    ],
)
