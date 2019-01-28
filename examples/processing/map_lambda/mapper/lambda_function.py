import json


def lambda_handler(event, context):

    # Read input file.
    # map it!

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Mapping complete'})
    }
