#!/usr/bin/env python
# Copyright (c) 2007 Qtrac Ltd. All rights reserved.
# This module is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.

import os
import ez_setup
ez_setup.use_setuptools()

from setuptools import setup

setup(name='avoid_disaster',
      version = '1.0',
      author="amix",
      author_email="amix@amix.dk",
      url="http://www.amix.dk/",
      classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      packages=['avoid_disaster', 'test'],
      platforms=["Any"],
      license="BSD",
      keywords='backups amazon s3',
      description="Implements a simple backup script to backup things to Amazon S3",
      long_description="""\
avoid_disaster
---------------

Implements a simple backup script to backup things to Amazon S3.
avoid_disaster be used to easily script daily, weekly or monthly backups.

For more information check out:
http://amix.dk/blog/post/19529#avoid-disaster-Easily-script-daily-or-weekly-backups-to-S3

Examples
----------

Backup test_dir to S3::

    import os
    from avoid_disaster import S3Uploader, gunzip_dir, generate_file_key

    #--- Globals ----------------------------------------------
    AWS_KEY = 'YOUR AWS KEY'
    AWS_SECRET = 'YOUR AWS SECRET'

    s3_uploader = S3Uploader(AWS_KEY,
                             AWS_SECRET,
                             'backups.your_domain.com')

    #--- Backup directory ----------------------------------------------
    file_key = generate_file_key('test_dir.%(weekday)s.tar.gz')

    gz_filename = gunzip_dir('test_dir/', file_key)

    s3_uploader.upload(file_key, gz_filename, delete_old=True)

    os.remove(gz_filename)

Copyright: 2010 by amix
License: BSD.""")
