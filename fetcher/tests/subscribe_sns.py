import os
from os.path import join,dirname
import sys
from pathlib import Path
sys.path.append("../../common/")
import utils as utl

import boto3
from dotenv import load_dotenv
from http.server import BaseHTTPRequestHandler, HTTPServer

load_dotenv()

# Constants
root_path = join(dirname(__file__),"../../..")
cache_path = join(root_path,"cache")

# Initialize the S3 client
s3 = boto3.client('s3',
                    aws_access_key_id=os.getenv('aws_access_key_id'),
                    aws_secret_access_key=os.getenv('aws_secret_access_key')
                )
sns = boto3.client('sns',
                    aws_access_key_id=os.getenv('aws_access_key_id'),
                    aws_secret_access_key=os.getenv('aws_secret_access_key')
                )

def subscribe_to_sns(topic_arn, endpoint_url):
    response = sns.subscribe(
            TopicArn=topic_arn,
            Protocol='https',
            Endpoint=endpoint_url  # This should be your server's public URL
        )
    return response

def main():
    subscribe_to_sns(os.getenv('AWS_SNS_ARN'),
                     os.getenv('AWS_SERVER_ENDPOINT'))

if __name__ == "__main__":
    main()
