Script backups easily to S3
===========================================

avoid_disaster be used to easily script daily, weekly or monthly backups and upload them to S3.

For more information check out:
http://amix.dk/blog/post/19529#avoid-disaster-Easily-script-daily-or-weekly-backups-to-S3
    
To install it do following:

    sudo easy_install boto
    sudo easy_install avoid_disaster


Examples
========

Example of creating a daily backup of test_dir/:

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
