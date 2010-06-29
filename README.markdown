Script backups easily to Amazon S3
===========================================

Avoid Disaster can be used to script daily, weekly or monthly backups and upload them to S3.

For more information check out: 

    [amix.dk: Avoid Disaster: Script backups easily to Amazon S3](http://amix.dk/blog/post/19529#avoid-disaster-Easily-script-daily-or-weekly-backups-to-S3) 
    
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

    #--- Globals ----------------------------------------------
    AWS_KEY = 'YOUR AWS KEY'
    AWS_SECRET = 'YOUR AWS SECRET'

    s3_uploader = S3Uploader(AWS_KEY,
                             AWS_SECRET,
                             'backups.wedoist.com')


    #--- Easy usage ----------------------------------------------
    #Daily backup
    s3_uploader.compress_and_upload('test_dir/',
                                    'test_dir.%(weekday)s.tar.gz',
                                    delete_old=True)

    #Monthly backup
    s3_uploader.compress_and_upload('test_dir/',
                                    'test_dir.%(month_name)s.tar.gz',
                                    delete_old=True)

    #Weekly backup
    s3_uploader.compress_and_upload('test_dir/',
                                    'test_dir.%(week_number)s.tar.gz',
                                    delete_old=True)


    #--- Generic usage ----------------------------------------------
    file_key = generate_file_key('test_dir.%(weekday)s.tar.gz')
    gz_filename = gunzip_dir('test_dir/', file_key)
    s3_uploader.upload(file_key, gz_filename, delete_old=True)
    os.remove(gz_filename)
