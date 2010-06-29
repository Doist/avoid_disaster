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
