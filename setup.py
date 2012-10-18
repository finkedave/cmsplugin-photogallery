#!/usr/bin/env python
import os
from setuptools import setup, find_packages

README_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                           'README.rst')

dependencies = [
    'simplejson==2.1.6',
    'django-filer==0.9',
    'django-cms==2.3.1',
]

setup(
    name='cmsplugin-photogallery',
    version='0.0.1',
    description='Photo Gallery CMS Plugin app',
    long_description = open(README_PATH, 'r').read(),
    author='TPG Audience Facing Team',
    author_email='tpg-pbs-userfacing@threepillarglobal.com',
    url='git@github.com:pbs/cms-newsletter-plugin.git',
    packages=find_packages(),
    include_package_data=True,
    install_requires = dependencies,
    setup_requires = ['s3sourceuploader',],
)