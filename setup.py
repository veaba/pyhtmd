# -*- coding:utf-8 -*-

####################################################
# File Name:steup.py
# Author: Veaba
# Mail: godpu@outlook.com
# Create Time: 2019年10月30日
####################################################

from setuptools import setup, find_packages

with open('README.md', 'r', encoding='UTF-8') as f:
    loog_description = f.read()
setup(
    name="pyhtmd",
    version="1.0.1",
    keywords=("html", 'markdown', "parser", "pyhtmd"),
    description="A Python HTML to Markdown parser",
    long_description=loog_description,
    long_description_content_type="text/markdown",
    url="https://github.com/veaba/pyhtmd",
    author="veaba",
    author_email="godpu@outlook.com",
    packages=find_packages(),
    include_package_data=True,
    platforms="any"
)
