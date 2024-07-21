import os
from os.path import join,dirname
import sys
from pathlib import Path
sys.path.append("../../common/")
import utils as utl

import boto3
from dotenv import load_dotenv

load_dotenv()

# Constants
root_path = join(dirname(__file__),"../../..")
cache_path = join(root_path,"cache")

# Initialize the S3 client
s3 = boto3.client('s3',
                    aws_access_key_id=os.getenv('aws_access_key_id'),
                    aws_secret_access_key=os.getenv('aws_secret_access_key')
                )

def s3_upload():
    bucket_name = "markdown-rag"
    key = "markdown-test.txt"
    content_string = "This is a test file"
    content_bytes = content_string.encode()  # Convert string to bytes
    s3.put_object(Bucket=bucket_name, Key=key, Body=content_bytes)
    print(f'Uploaded {key} to {bucket_name}')
    return

def s3_download(entry):
    bucket_name = entry["bucket"]
    key = entry["key"]
    dest = entry["dest"]
    # Download the file
    download_path = 'downloaded_test.txt'
    s3.download_file(bucket_name, key, download_path)
    print(f'Downloaded {key} to {download_path}')
    # Ensure the content matches
    with open(download_path, 'rb') as f:
        content = f.read()
    assert content == b'This is a test file'
    print('File content matches!')
    return


def main():
    # Load YAML configuration
    manifest = utl.load_yaml(join(root_path,'manifest.yaml'))
    fetch_list = manifest["fetcher"]
    for entry in fetch_list:
        if (entry["type"] == "sws_s3"):
            print("Fetching from s3 bucket:", entry['bucket'])
            s3_download(entry)

if __name__ == "__main__":
    s3_upload()
