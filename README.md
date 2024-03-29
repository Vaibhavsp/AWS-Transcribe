
# Automated Transcription with AWS: S3, Lambda, and Transcribe

### Overview

#### 🔗 What is Amazon Transcribe?  
✔ Extract key business insights from customer calls, video files, clinical conversations, and more.  
✔ Improve business outcomes with state of the art speech recognition models that are fully managed and continuously trained.  
✔ Enhance accuracy with custom models that understand your domain specific vocabulary.  
✔ Ensure customer privacy and safety by masking sensitive information.


#### 🔗 What is Amazon S3?  
✔ Amazon S3 is an object storage service that offers industry-leading scalability, data availability, security, and performance.  
✔ Store and protect any amount of data for a range of use cases, such as data lakes, websites, cloud-native applications, backups, archive, machine learning, and analytics.  
✔ Amazon S3 is designed for 99.999999999% (11 9's) of durability, and stores data for millions of customers all around the world.


#### 🔗 What is AWS Lambda  
✔ Run code without provisioning or managing servers, creating workload-aware cluster scaling logic, maintaining event integrations, or managing runtimes.  
✔ Run code for virtually any type of application or backend service. Just upload your code as a ZIP file or container image, and Lambda automatically allocates compute execution power and runs your code based on the incoming request or event, for any scale of traffic.  
✔ Write Lambda functions in your favorite language (Node.js, Python, Go, Java, and more) and use both serverless and container tools, such as AWS SAM or Docker CLI, to build, test, and deploy your functions.


## Project Description



Welcome to our mini-project leveraging AWS services, focusing on AWS Transcribe, a powerful tool for converting audio and video files into text format.



#### The workflow of our project is as follows:

1. User uploads audio or video files to the designated S3 Source Bucket.
2. An AWS Lambda Function is triggered automatically upon file upload to the S3 Source Bucket.
3. The Lambda Function executes the designated code.
4. The Lambda Function initiates a speech-to-text batch job using AWS Transcribe.
5. AWS Transcribe processes the audio or video files and saves the resulting .json transcription file into the specified S3 Target Bucket.
6. Users can conveniently download the transcription file from the S3 Target Bucket for further use.

   This project streamlines the process of transcribing audio and video files into text using AWS Transcribe, offering a seamless solution for various transcription needs.
## Lambda Function

To deploy this project run followig python code in Lambda

```bash
import json
import boto3

mytranscribefunc = boto3.client("transcribe",
                        aws_access_key_id="xxxxxxxxx",
                        aws_secret_access_key="xxxxxxxxxxxxxxxxxxx",
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
```


## Demo Images

### Create S3 Buckets for Storing Input and Output and Create a Lambda Event

![S3 Buckets](https://github.com/Vaibhavsp/AWS-Transcribe/assets/100761402/3d1787e2-72f0-4a06-a4c2-6fb75d1e09e9)

### Tirggered S3 is shown 

![Lambda 1](https://github.com/Vaibhavsp/AWS-Transcribe/assets/100761402/aca1f9b5-4d06-4e31-acd7-688b14796f2c)

### Write a Lambda Function code

![Lambda 2](https://github.com/Vaibhavsp/AWS-Transcribe/assets/100761402/54bb9338-3b27-4326-b13e-4921cf4170c4)

### Add Input File in your Input Bucket

![S3 ip](https://github.com/Vaibhavsp/AWS-Transcribe/assets/100761402/ea7b0527-75b6-44d1-bc67-b974d16eabce)

### Check CloudWatch weather Lambda Function works or not

![CloudWatch](https://github.com/Vaibhavsp/AWS-Transcribe/assets/100761402/a1879ce8-6253-4161-98f5-07519e3afb0f)

### If Lambda Function works correctly; it creates Transcription Job

![Transcribe](https://github.com/Vaibhavsp/AWS-Transcribe/assets/100761402/615a9f5f-f37f-499a-8c20-4376628f9103)

### Finally, Transcription Job provides an Output File to your Output Bucket

![S3 op](https://github.com/Vaibhavsp/AWS-Transcribe/assets/100761402/8d87ba66-e805-469f-857a-ce9c41891c86)

## Documentation

[AWS Transcribe Documentation](https://docs.aws.amazon.com/transcribe/)

[AWS Lambda Documentation](https://docs.aws.amazon.com/lambda/)

[AWS S3 Documentation](https://docs.aws.amazon.com/s3/)

[AWS Boto3 Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)

[start_transcription_job Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe/client/start_transcription_job.html)

## Tech Stack

**Client:** S3, Lambda, CloudWatch, AWS Transcribe


## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/vaibhav-parekh08/)


[![linkedin](https://img.shields.io/badge/Hashnode-2962FF?style=for-the-badge&logo=hashnode&logoColor=white)](https://hashnode.com/@Vaibhav19)
