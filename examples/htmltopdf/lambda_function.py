import pdfkit
import boto3

s3 = boto3.client('s3')


def lambda_handler(event, context):
    pdfkit.from_url('http://google.com', '/tmp/out.pdf')

    with open('/tmp/out.pdf', 'rb') as f:
        response = s3.put_object(
            Bucket='temp-awseabsgddev',
            Key='juni/google.pdf',
            Body=f.read()
        )

    return {'response': response}
