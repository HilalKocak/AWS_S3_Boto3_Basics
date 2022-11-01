import boto3
client=boto3.client('s3')
s3=boto3.resource('s3')

bucketname="kocakboto3bucket"

responce=client.delete_bucket(
    Bucket=bucketname
)