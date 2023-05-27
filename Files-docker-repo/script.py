
import boto3
import json
from datetime import datetime

def generate_data():

    file_content = {
    'key1': 'value1',
    'key2': 'value2',
    'key3': 'value3'}

    s3 = boto3.client('s3')
    # Get the current datetime and seconds
    current_datetime = datetime.now()
    seconds = current_datetime.second
    
    # Define the bucket name and file name
    bucket_name = 'ecs-trigger-bucket'
    file_name = f'file_content_{current_datetime.strftime("%Y%m%d_%H%M%S")}.json'

    # Convert the dictionary to JSON string
    file_content_json = json.dumps(file_content)
    # Upload the JSON file to S3
    s3.put_object(Body=file_content_json, Bucket=bucket_name, Key=file_name)

generate_data()

