#!/usr/bin/python
# -*- coding: utf-8 -*-

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license

from distutils.core import setup

setup(
    name = "thumbor_mongodb_loader",
    packages = ["thumbor_mongodb_loader"],
    version = "1.2.0",
    description = "MongoDB GridFS loader for Thumbor - Jeunesse Francetv Release",
    author = "Bertrand Thill",
    author_email = "bertrand.thill@francetv.fr",
    keywords = ["thumbor", "mongodb", "images", "gridfs"],
    license = 'MIT',
    url = 'https://github.com/francetv/thumbor_mongodb_loader',
    classifiers = ['Development Status :: 4 - Beta',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT License',
                   'Natural Language :: English',
                   'Operating System :: POSIX :: Linux',
                   'Programming Language :: Python :: 2.7',
                   'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
                   'Topic :: Multimedia :: Graphics :: Presentation'
    ],
    package_dir = {"thumbor_mongodb_loader": "thumbor_mongodb_loader"},
    install_requires=['thumbor>=6.5.0','pymongo>=3.4.0'],
    long_description = """\
This module provide support for MongoDB GridFS loader.
Image data is addressed by its ObjectId('path')
"""
)