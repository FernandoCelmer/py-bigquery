#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup
from setuptools.command.install import install
from py_bigquery import __version__


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


class CustomInstallCommand(install):
    def run(self):
        install.run(self)


setup(
    name="py-bigquery",
    version=__version__,
    author="Fernando Celmer",
    author_email="email@fernandocelmer.com",
    description="Python BigQuery",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FernandoCelmer/py-bigquery",
    classifiers=[
        'Development Status :: 4 - Beta',
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        'Intended Audience :: Developers',
        'Natural Language :: English',
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    packages=['bigquery_orm'],
    include_package_data=True,
    install_requires=[
        'google-auth',
        'google-cloud-bigquery'
    ],
    python_requires=">=3.10",
    zip_safe=True,
    fullname='py-bigquery',
    entry_points={
        'console_scripts': ['bigquery=py_bigquery.main:main'],
    },
)
