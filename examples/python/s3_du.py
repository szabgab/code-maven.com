import os
import boto3
s3 = boto3.client('s3')

def list_buckets():
   resp = s3.list_buckets()
   #print(resp.keys()) # [u'Owner', u'Buckets', 'ResponseMetadata']
   #print(resp['Buckets'])
   for bucket in resp['Buckets']:
       #print(bucket)    #   {u'CreationDate': datetime.datetime(2017, 11, 15, 13, 39, 31, tzinfo=tzutc()), u'Name': 'name-of-the-bucket'}
       process_bucket(bucket['Name'])

def process_bucket(bucket):
   print(bucket)
   last_entry = ''
   count = 0
   size = 0
   dirs = {}
   while True:
       objects = s3.list_objects_v2(
           Bucket     = bucket,
           StartAfter = last_entry,
       )
       #print(objects.keys())
       #print(objects['MaxKeys'])
       #print(objects['Contents'])
       if 'Contents' not in objects:
           #print(objects)
           break
       if len(objects['Contents']) == 0:
           break
       count += len(objects['Contents'])
       for obj in objects['Contents']:
           #print(obj)
           dirname = os.path.dirname(obj['Key']) + '/'
           if dirname not in dirs:
               dirs[dirname] = {
                   'size' : 0,
                   'count' : 0,
               }
           dirs[dirname]['count'] += 1
           dirs[dirname]['size'] += obj['Size']
           size += obj['Size']
       last_entry = objects['Contents'][-1]['Key']

   with open('bucket_sizes.txt', 'a') as fh:
       fh.write("{},{},{}\n".format(bucket, count, size))
   with open('sizes.txt', 'a') as fh:
       fh.write("{},{},{}\n".format(bucket, count, size))
       for path in sorted(dirs.keys()):
           fh.write("{},{},{}\n".format(path, dirs[path]['count'], dirs[path]['size']))
   #print(count)
   #print(size)

list_buckets()

