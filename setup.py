#!/usr/bin/env python
#-*- coding:utf-8 -*-

from setuptools import setup, find_packages

setup(
    name = "HydroXAJ_test",
    version = "0.0.2",
    keywords = ["hydrologic model", "XinAnJiang"],
    description = "A conceptual hydrological model.",
    long_description = "This is a python implementation for XinAnJiang (XAJ) model, which is one of the most famous conceptual hydrological model, especially in Southern China.",

    url = "https://github.com/OuyangWenyu/hydro-model-xaj",
    author = "OuyangWenyu",
    author_email = "wenyuouyang@outlook.com",
    license= "MIT license ",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = ["numpy",
                        "pandas",
                        "deap",
                        "spotpy",
                        "seaborn",
                        "tqdm",
                        "sphinx",
                        "pytest",
                        "black"],

)