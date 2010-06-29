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
