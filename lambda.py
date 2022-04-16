import json
import base64
import sys
import boto3
import io
from io import BytesIO
import re
import base64
from PIL import Image
from botocore.exceptions import NoCredentialsError



s3 = boto3.client('s3')
def lambda_handler(event, context):
    dec = event['image']
    buffer = BytesIO()
    im = Image.open(BytesIO(base64.b64decode(dec + "-")))
    print("im = Image.open(BytesIO(base64.b64decode")
    in_mem_file = io.BytesIO()
    print("in_mem_file = io.BytesIO()")
    im.save(in_mem_file, format=im.format)
    print("im.save(in_mem_file, format=im.format)")
    in_mem_file.seek(0)
    print("in_mem_file.seek(0)")
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)
    print(" in_mem_file.seek(0)")
    try:
        print("ici")
        #s3.put_object(Body=buffer, Bucket='dataset-fyc', Key='t.jpeg',  ContentType='image/jpeg')
        s3.upload_fileobj(in_mem_file,'dataset-fyc', Key='t.jpeg', ExtraArgs={
        'ACL': 'public-read'
    })
        print("ici2")
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False            
    except Exception as e:
        print(e)



   
        
        
        
