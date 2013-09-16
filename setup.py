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
      version = '1.3',
      author="amix",
      author_email="amix@amix.dk",
      url="http://www.amix.dk/",
      classifiers=[
        "Development Status :: 5 - Production/Stable",
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
      description="Script backups easily to Amazon S3",
      long_description="""\
avoid_disaster
---------------

Avoid Disaster can be used to script daily, weekly or monthly backups and upload them to S3.

For more information check out:
http://amix.dk/blog/post/19529#Avoid-Disaster-Script-backups-easily-to-Amazon-S3

Examples
----------

Example of creating a backups of test_dir/::

    import os
    from avoid_disaster import S3Uploader, gunzip_dir, generate_file_key

    #--- Globals ----------------------------------------------
    AWS_KEY = 'YOUR AWS KEY'
    AWS_SECRET = 'YOUR AWS SECRET'

    s3_uploader = S3Uploader(AWS_KEY,
                             AWS_SECRET,
                             'backups.your_domain.com')

    #--- Easy usage ----------------------------------------------
    #Daily
    s3_uploader.compress_and_upload('test_dir/',
                                    'test_dir.%(weekday)s.tgz',
                                    replace_old=True)

    #Monthly
    s3_uploader.compress_and_upload('test_dir/',
                                    'test_dir.%(month_name)s.tgz',
                                    replace_old=True)

    #Weekly
    s3_uploader.compress_and_upload('test_dir/',
                                    'test_dir.%(week_number)s.tgz',
                                    replace_old=True)


    #--- Generic usage ----------------------------------------------
    file_key = generate_file_key('test_dir.%(weekday)s.tgz')
    gz_filename = gunzip_dir('test_dir/', file_key)
    s3_uploader.upload(file_key, gz_filename, replace_old=True)
    os.remove(gz_filename)

Copyright: 2010 by amix
License: BSD.""")
