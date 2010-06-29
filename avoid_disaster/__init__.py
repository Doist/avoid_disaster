# -*- coding: utf-8 -*-
"""
avoid_disaster
~~~~~~~~

Implements a simple backup script to backup things to Amazon S3.
avoid_disaster be used to easily script daily, weekly or monthly backups.

Example of usage::

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

:copyright: 2010 by amix
:license: BSD, see LICENSE for more details."""
import os, sys
from datetime import datetime

from boto.s3.connection import S3Connection
from boto.s3.key import Key

class S3Uploader:
    """A simpler uploader to S3 using boto library."""

    def __init__(self, aws_key, aws_secret, bucket_name):
        self.connection = S3Connection(aws_key, aws_secret)
        self.bucket = self.connection.get_bucket(bucket_name)

    def upload(self, filekey, filename, delete_old=False):
        if not delete_old:
            if self.has_file(filekey):
                print 'ERROR: File already found.'
                sys.exit(-1)

        key = Key(self.bucket)
        key.key = filekey

        key.set_contents_from_filename(filename,
                                       {},
                                       replace=True)

    def has_file(self, filekey):
        return self.bucket.get_key(filekey)

    def delete_file(self, filekey):
        return self.bucket.delete_key(filekey)


def generate_file_key(filename):
    """Helper to generate daily backups.

    Example of usage::
        generate_file_key('my_backup.%(weekday)s.tar.gz')

    """
    now = datetime.utcnow()
    common = {
        'weekday': now.strftime("%A"),
        'month': now.strftime("%B"),
        'week': now.strftime("%U")
    }
    return filename % common


def gunzip_dir(directory, output_filename):
    """Helper to tar and gunzip a directory.

    TODO: Should probably use subprocess."""
    directory = os.path.realpath(directory)
    cmd = 'tar -cvf - "%s" | gzip -c > "%s"' % (directory, output_filename)

    print 'Running... %s' % cmd
    r_code = os.system(cmd)

    if r_code != 0:
        print 'ERROR: Could not compress.'
        sys.exit(-1)
    else:
        return output_filename
