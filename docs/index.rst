.. juniper documentation master file, created by
   sphinx-quickstart on Tue Jan 29 17:16:07 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to juniper's documentation!
===================================

Welcome to Juniper's documentation. Get started with :doc:`quickstart`. There is also a
more detailed :doc:`tutorial` that shows how to package a set of lambda
functions using juniper. Common patterns are described in the :doc:`concepts`
section.

Packaging Lambda
****************

Packaging of **python** lambda functions is a problem a web developer faces when
building web APIs using AWS services. The main issue is that the dependencies
of the function must be included along with the business logic of the function.

The `AWS documentation`_ provides a clear set of steps that a developer must take
in order to package a single lambda function that has a set of dependencies. The
dependencies must be specified in a requirements.txt file. The steps as defined
in the documentation are the following:

1. Create a virtual environment.
2. Activate the environment
3. Install libraries with pip
4. Deactivate the virtual environment.
5. Create a ZIP archive with the contents of the site-packages directory
6. Add your function code to the archive.

When working with a simple lambda function, taking these set of steps is not a
complicated undertaking. It is inconvenient, but a process that can be easily
scripted.

With this particular approach, scalability becomes the bottleneck. In the real world
a developer needs to package not only one, but 3 or 4 functions at a time. Also,
using your local machine as a way to generate the zip artifact is not always desirable.
A package that you can build and put in the zip using your own setup might not work
once you deploy it to AWS.

For these reasons, and for several other that will become clear, Juniper was born.

.. _AWS Documentation: https://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html

What is Juniper?
****************

Juniper is a packaging tool with a with a single purpose in mind: stream and standardize
the creation of a zip artifact for a set of lambda functions.

As a developer working with AWS Lambda functions, the only thing you need to do
is create a manifest file like this one:

.. code:: yaml

    functions:
      processor:    # <- Name of your function
        requirements: ./src/processor/requirements.txt
        include:
        - ./src/commonlib           # Include this module in the zip
        - ./src/processor/first     # Include this module in the zip

With the basic information about your lambda functions, use juniper to generate
the zip files for your functions:

    >>> juni build

The command will create a `processor.zip` with the dependencies defined in the
requirements file and the entire commonlib.

With SAM
********

If you are working with lambda functions, chances are that you are using a `SAM`_
template as a way to define your serverless application. The template in its most
basic form looks like:

.. _SAM: https://github.com/awslabs/serverless-application-model

.. code:: yaml

    Transform: 'AWS::Serverless-2016-10-31'
    Resources:

    ProcessorFn:
        # This resource creates a Lambda function.
        Type: 'AWS::Serverless::Function'

        Properties:

        # The location of the Lambda function code.
        CodeUri: ./dist/processor.zip

Juniper, will build the zip file that you need to provide in order to update or create your
lambda function. It's your responsibility to use that file however you see fit.
You can use it in conjunction with your SAM template; as seen above, or you can
also use it to update a lambda function directly using the cli:

    >>> aws lambda update-function-code --function-name ProcessorFn --zip-file ./dist/processor.zip

Features
********

Using the available tools in the serverless space, we found there was no tool
capable of fulfilling all of these business needs:

* Minimal manifest file to define packaging
* Using docker containers as a way to install dependencies and generate the artifacts
* Ability to tailor the requirements.txt per lambda
* Create an individual zip artifact for multiple lambda functions
* Ability to include shared dependencies (python modules relative to the function
  being packaged)

This list defines the entire scope of Juniper.

.. note::

    Keep in mind that Juniper is a packaging tool only! Most of the tools surveyed
    offer a more comprehensive set of features one of which is packaging.

Contents:
=========

.. toctree::
    :maxdepth: 2
    :numbered:
    :glob:

    quickstart.rst
    tutorial.rst
    concepts.rst
