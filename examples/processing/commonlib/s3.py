import json
import boto3

_s3_client = boto3.client('s3')


def read_json_file(bucket, key):
    """
    Reads a JSON file from s3.
    :params bucket: The name of the bucket where the source file is at.
    :params key: The full file name of the object to read.
    """

    response = _s3_client.get_object(
        Bucket=bucket,
        Key=key
    )

    return json.load(response['Body'])


def write_json_file(bucket, key, data):
    """
    Write a JSON file to an s3 bucket.

    :params bucket: The name of the bucket where the source file is at.
    :params key: The full file name of the object to write.
    :param data: The json object to add to the bucket.
    """

    return _s3_client.put_object(
        Bucket=bucket,
        Key=key,
        Body=json.dumps(data).encode()
    )
