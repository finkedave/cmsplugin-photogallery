#!/usr/bin/env python
from setuptools import setup, find_packages

dependencies = [
    'simplejson==2.1.6',
]

setup(
    name='cms-newsletter-plugin',
    version='1.1.1',
    description='Newsletter Plugin app',
    author='TPG Audience Facing Team',
    author_email='tpg-pbs-userfacing@threepillarglobal.com',
    url='git@github.com:pbs/cms-newsletter-plugin.git',
    packages=find_packages(),
    include_package_data=True,
    install_requires = dependencies,
    setup_requires = ['s3sourceuploader',],
)
