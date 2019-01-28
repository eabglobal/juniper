import json
from commonlib import s3
from splitter.constants import BUCKET_NAME


def lambda_handler(event, context):
    """
    Reads a source file from s3, splits the contents of the file in two and
    adds the resulting values in the same bucket.
    """

    file_name = event.get('source_file')

    data = s3.read_json_file(BUCKET_NAME, file_name)
    split_point = len(data) // 2

    s3.write_json_file(BUCKET_NAME, 'to_map/part1.json', data[:split_point])
    s3.write_json_file(BUCKET_NAME, 'to_map/part2.json', data[split_point:])

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Created 2 files'})
    }
