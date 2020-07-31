#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    setup.py.py
# @Author:      manunellutla
# @Time:        6/8/20 10:14 PM

import setuptools

with open("Readme.md", "r") as rmd:
    long_description = rmd.read();

setuptools.setup(
    name="MyTestPackage",
    version="0.0.1",
    author="Example Author",
    author_email="author@example.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
