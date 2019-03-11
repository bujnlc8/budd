# coding=utf-8

from setuptools import setup, find_packages


setup(name="budd",
    version="0.0.1",
    url="https://github.com/linghaihui/budd",
    license="MIT",
    author="linghaihui",
    author_email="haihuiling2014@gmail.com",
    description="A simple env collector",
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    zip_safe=False,)
