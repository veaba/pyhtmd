#
#-*- coding:utf-8 -*-

####################################################
# File Name:steup.py
# Author: Veaba
# Mail: godpu@outlook.com
# Create Time: 2019年10月30日
####################################################

from setuptools import setup,find_packages

setup(
    name="pyhtmd",
    version="0.1.0",
    keywords=("html",'markdown',"parser","pyhtmd"),
    description="A Python HTML to Markdown parser",
    long_description="A Python HTML to Markdown parser, without using any third-party dependency.（一款Python版本的HTML转markdown解析器，不使用任何第三方工具）",
    libraries="MIT Licence",
    url="https://github.com/veaba/pyhtmd",
    author="veaba",
    author_email="godpu@outlook.com",
    packages=find_packages(),
    include_package_data=True,
    platforms="any"
)