Tutorial
========

Juniper comes with a set of examples meant to show a developer working in the
serverless domain, what he/she needs to do in order to easily adopt the tool.

To get started, make sure you clone the project and install juni:

    >>> git clone git@github.com:eabglobal/juniper.git
    >>> cd juniper
    >>> python3 -m venv venv
    >>> source venv/bin/activate
    >>> pip install -e .
    >>> cd examples/processing

Map Reduce Pipeline
*******************

The processing example is based on a map reduce pipeline in which the developer
has defined multiple lambda functions. The first lambda function in the processing
pipeline is the split_lambda. This function will be triggered whenever a json object
is added to S3, the function will read the file and it will split it into two files.

The entire business logic associated with that function is:

.. code:: python

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

Note that this function has a reference to the `commonlib.s3` object. The
commonlib module lives along side the `split_lambda` function and it must be included
in the split_lambda.zip artifact. Otherwise, the function will fail with a reference
not found error.

The business logic of the remaining functions in the pipeline is not relevant
to the example, however, the folder structure has a set of placeholders for them.

The *manifest* file, for the generation of the artifacts of this pipeline looks like:

.. literalinclude:: ../examples/processing/manifest.yml
    :emphasize-lines: 6

Note that in the definition of the `split_step` the includes section makes reference
to the `commonlib`. This line indicates to juniper that the codebase inside the commonlib
folder must be included in the .zip artifact for the split function.

>>> juni build
Removing processing_map_step-lambda_1    ... done
Removing processing_split_step-lambda_1  ... done
Removing processing_reduce_step-lambda_1 ... done
Removing network processing_default
Creating network "processing_default" with the default driver
Creating processing_split_step-lambda_1  ... done
Creating processing_map_step-lambda_1    ... done
Creating processing_reduce_step-lambda_1 ... done
Attaching to processing_split_step-lambda_1, processing_map_step-lambda_1, processing_reduce_step-lambda_1
split_step-lambda_1   | Starting to package split_step
reduce_step-lambda_1  | Starting to package reduce_step
map_step-lambda_1     | Starting to package map_step
reduce_step-lambda_1  | Finished packaging
processing_reduce_step-lambda_1 exited with code 0
split_step-lambda_1   | Finished packaging
processing_split_step-lambda_1 exited with code 0
map_step-lambda_1     | Finished packaging
processing_map_step-lambda_1 exited with code 0

Without any arguments, juni will by default look for a file named `manifest.yml`.
From that file, juni will create the artifacts in a `./dist` folder. The output
of the above command creates the following artifacts:

>>> tree dist
dist
├── map_step.zip
├── reduce_step.zip
└── split_step.zip

Unzipping the `split_step` lambda we expect to have the contents of pip installing
the request library; given that it is defined in the requirements.txt. The contents
of the common lib and finally the `splitter`. All of which are defined in the
manifest file.

>>> ls -larth
drwx------  10 pdiazvargas  375838832   320B Jan 30 22:27 .
drwxr-xr-x   7 pdiazvargas  375838832   224B Jan 30 22:27 ..
drwxr-xr-x  15 pdiazvargas  375838832   480B Jan 31  2019 urllib3
drwxr-xr-x   4 pdiazvargas  375838832   128B Jan 31  2019 splitter
drwxr-xr-x  20 pdiazvargas  375838832   640B Jan 31  2019 requests
drwxr-xr-x  10 pdiazvargas  375838832   320B Jan 31  2019 idna
drwxr-xr-x   4 pdiazvargas  375838832   128B Jan 31  2019 commonlib
drwxr-xr-x  42 pdiazvargas  375838832   1.3K Jan 31  2019 chardet
drwxr-xr-x   6 pdiazvargas  375838832   192B Jan 31  2019 certifi
drwxr-xr-x   3 pdiazvargas  375838832    96B Jan 31  2019 bin
