# -*- coding: utf-8 -*-
"""
avoid_disaster
~~~~~~~~

Avoid Disaster can be used to script daily, weekly or monthly backups and upload them to S3.

More info:
    http://amix.dk/blog/post/19529#Avoid-Disaster-Script-backups-easily-to-S3

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

    def compress_and_upload(self, directory, filename, replace_old=False,
                                  temp_dir='/tmp'):
        """Helper function that gunzips `directory`, generates a filekey from `filename`,
        uploads it to S3 and deletes the gunzip.

        Will as default store temp files in `temp_dir` (/tmp).
        """
        file_key = generate_file_key(filename)
        gz_filename = gunzip_dir(directory, os.path.join(temp_dir, file_key))

        try:
            self.upload(file_key, gz_filename, replace_old=replace_old)
        finally:
            os.remove(gz_filename)

    def upload(self, filekey, filename, replace_old=False):
        """Upload `filename` as `filekey`.
        If `replace_old` is True then the old key is replaced,
        else an error is thrown on duplicates.
        """
        if not replace_old:
            if self.has_file(filekey):
                print 'ERROR: File already found.'
                sys.exit(-1)

        key = Key(self.bucket)
        key.key = filekey

        key.set_contents_from_filename(filename,
                                       {},
                                       replace=True)

    def has_file(self, filekey):
        """Return True if `filekey` is found."""
        return self.bucket.get_key(filekey)

    def delete_file(self, filekey):
        """Deletes `filekey` from the bucket."""
        return self.bucket.delete_key(filekey)


def generate_file_key(filename):
    """Helper to generate daily backups.

    Example of usage::
        generate_file_key('my_backup.%(weekday)s.tgz')
    """
    now = datetime.utcnow()
    common = {
        'weekday': now.strftime("%A"),
        'month_name': now.strftime("%B"),
        'week_number': now.strftime("%U")
    }
    return filename % common


def gunzip_dir(directory, output_filename):
    """Helper to tar and gunzip a directory.

    TODO: Should probably use subprocess.
    """
    directory = os.path.realpath(directory)
    cmd = 'tar czPf "%s" "%s"' % (output_filename, directory)

    print 'Running... %s' % cmd
    r_code = os.system(cmd)

    if r_code != 0:
        print 'ERROR: Could not compress.'
        sys.exit(-1)
    else:
        return output_filename
