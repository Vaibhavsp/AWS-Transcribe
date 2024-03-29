import json
import boto3

mytranscribefunc = boto3.client("transcribe",
                        aws_access_key_id="xxxxxxxxxxxxxxxxxx",
                        aws_secret_access_key="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                        region_name="ap-south-1",
                        )

def lambda_handler(event, context):
    
    bucketName = event['Records'][0]['s3']['bucket']['name']
    
    fileName = event['Records'][0]['s3']['object']['key']
    
    finalURL = "s3://" + bucketName + "/" + fileName
    
    print(finalURL)
    
    response = mytranscribefunc.start_transcription_job(
                TranscriptionJobName="mytranscribejob",
                LanguageCode="en-US",
                MediaFormat="mp4",
                Media = {
                        'MediaFileUri': finalURL
                        },
                OutputBucketName='transcribe-proj-op',
                OutputKey='final-transcribe.json',
                )
                
    print(response)
    
    print("Hello...")
    print(event)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }