import json


def lambda_handler(event, context):

    # Read input files.
    # combine them!

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Reducing complete'})
    }
