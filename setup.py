#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
        name = 'podgen',
        packages = ['podgen'],
        # Remember to update the version in podgen.version, too!
        version = '1.0.0',
        description = 'Generating podcasts with Python should be easy!',
        author = 'Thorben W. S. Dahl',
        author_email = 'thorben@sjostrom.no',
        url = 'http://podgen.readthedocs.io/en/latest/',
        keywords = ['feed', 'RSS', 'podcast', 'iTunes', 'generator'],
        license = 'FreeBSD and LGPLv3+',
        install_requires = ['lxml', 
                            'python-dateutil', 
                            'future', 
                            'pytz', 
                            'tinytag',
                            'requests'],
        classifiers = [
            'Development Status :: 5 - Production/Stable',
            'Intended Audience :: Developers',
            'Intended Audience :: Information Technology',
            'Intended Audience :: Science/Research',
            'License :: OSI Approved :: BSD License',
            'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
            'Natural Language :: English',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Topic :: Communications',
            'Topic :: Internet',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Topic :: Text Processing',
            'Topic :: Text Processing :: Markup',
            'Topic :: Text Processing :: Markup :: XML'
            ],
        long_description = '''\
PodGen
======

This module can be used to easily generate Podcasts. It is designed so you
don't need to read up on how RSS and iTunes functions – it just works!

See the documentation at http://podgen.readthedocs.io/en/latest/ for more
information.

It is licensed under the terms of both the FreeBSD license and the LGPLv3+.
Choose the one which is more convenient for you. For more details have a look
at license.bsd and license.lgpl.
'''
)
