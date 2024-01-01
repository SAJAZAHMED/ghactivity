import os
from data_ingestion import ingest_data
import boto3
import data_ingestion


def lambda_handler(event, context):
    content = ingest_data() 

    os.environ.setdefault("AWS_PROFILE", "awsdemo")
    s3_client = boto3.client('s3')

    s3_client.put_object(
        Bucket='ghactivity-data',
        Body=content,
        Key=data_ingestion.file_name
    )

    objects = s3_client.list_objects_v2(Bucket='ghactivity-data')
    result_file=[]
    for object in objects['Contents']:
        result_file.append(object['Key'])


    print(result_file)







