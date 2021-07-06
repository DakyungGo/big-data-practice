import os
import boto3
import time
import sys
import bz2

session = boto3.Session(profile_name='default')
s3 = session.client('s3')

def download(s3, bucket, obj, local_file_path):
    s3.download_file(bucket, obj, local_file_path)

def upload(s3, local_file_path, bucket, obj):
    s3.upload_file(local_file_path, bucket, obj)

def make_public_read(s3, bucket, key):
    s3.put_object_acl(ACL='public-read', Bucket=bucket, Key=key)

def compress(file_path):
    with open(file_path, 'rb') as f_read:
        with open(file_path + '.bz2', 'wb') as f_write:
            f_write.write(bz2.compress(f_read.read()))


local_file_path = sys.argv[1]
today = time.strftime('%Y/%m-%d')
ispublic = sys.argv[2]
iscompress = sys.argv[3]
isdownload = sys.argv[4]
print(sys.argv)

for bucket in s3.list_buckets()['Buckets']:
    current = bucket['Name']

file_list = os.listdir(local_file_path)
for file in file_list:
    file_path = os.path.join(local_file_path, file)
    if not os.path.isfile(file_path):  # 폴더 스킵
        continue
    
    if iscompress == '1':
        # 파일 압축
        compress(file_path)
        print(today+'/'+file+'.bz2')
        #오늘 날짜 폴더에 업로드
        upload(s3, file_path, current, today+'/'+file+'.bz2')

    if ispublic == '1':
        make_public_read(s3, current, today+'/'+file+'.bz2')



if isdownload == '1':
    for key in s3.list_objects(Bucket=current)['Contents']:
        key_list = key['Key'].split('/')
        dir_name = "/".join(key_list[:-1])
        
        # Size가 0이면 폴더
        if key['Size']==0:
            continue
        os.makedirs(local_file_path+'/'+dir_name, exist_ok=True)
        download(s3, current, key['Key'], local_file_path+'/'+key['Key'])
    
    






