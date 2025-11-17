import boto3
import logging
from botocore.exceptions import ClientError


# Set param values
local_file_path= "C:/Users/LENOVO/Desktop/Learn Data Engineering/AWS-glue-data-ingestion/The Worlds Billionaires Dataset.csv"
bucket_name= 'glue-data-ingestion-pipeline'
s3_file= 'raw/billionairesData/world-billionaires-dataset.csv'


logging.info("Uploading file: STARTED")

# Upload the file
s3 = boto3.client(
    's3',
    region_name='ap-south-1'
)
try:
    s3.upload_file(local_file_path, bucket_name, s3_file)
    logging.info("File upload: SUCCESSFULLY")
except ClientError as e:
    logging.error(e)   
except FileNotFoundError:
    logging.error("File not found - ERROR")