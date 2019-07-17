#!/usr/bin/env python3

from setuptools import find_packages, setup

setup(
    name="textbisect",
    version="0.1.0.dev0",
    license="GPL3",
    description="Binary search in a sorted text file",
    author="Antonis Christofides",
    author_email="antonis@antonischristofides.com",
    url="https://github.com/openmeteo/textbisect",
    packages=find_packages(),
    test_suite="tests",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        (
            "License :: OSI Approved :: GNU General Public License "
            "v3 or later (GPLv3+)"
        ),
        "Topic :: Text Processing :: Indexing",
    ],
)
