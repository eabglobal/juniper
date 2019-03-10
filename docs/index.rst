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

Packaging λ
***********

Packaging of **python** lambda functions is a problem a web developer faces when
building web APIs using AWS services. The main issue is that the dependencies
of the function must be included along with the business logic of the function.

Creating the .zip artifacts manually is not a very complicated process, the steps
are clearly defined in the `AWS Documentation`_. However, when building a real
world serverless applications with lambda, this process is not very scalable.
Instead of building custom bash scripts to automate the build process, use juniper!

What is Juniper?
****************

Juniper is a packaging tool with a with a single purpose in mind: standardize
the creation of a zip artifact for a set of AWS Lambda functions.

To package a lambda function you must create a manifest file. This file tells juniper
what to include in the artifact. The definition of a single function looks like this:

.. code:: yaml

    functions:
      # Name of your lambda function
      processor:
        requirements: ./src/processor/requirements.txt
        include:
        # List of modules to include in the zip file.
        - ./src/commonlib
        - ./src/processor

With a manifest file like the one above, use the juniper cli to generate
the zip files for your functions:

    >>> juni build

Out of the box juniper will look for a definitions file called **manifest.yml**
and it will place the generated zip files in a **./dist** directory. These are
configurable parameters, to learn more read the :doc:`advanced`.

In this example, juni will create a `./dist/processor.zip` with the dependencies defined in the
requirements file and the contents of the ./src/commonlib and the ./src/processor.

With SAM
********

If you are working with lambda functions, chances are that you are using a `SAM`_
template as a way to define your AWS serverless resources. The definition of
a SAM template for a python lambda function looks like this:

.. code:: yaml

    Transform: 'AWS::Serverless-2016-10-31'
    Resources:

    ProcessorFn:
      # This resource creates a Lambda function.
      Type: 'AWS::Serverless::Function'

      Properties:
          # The location of the Lambda function code.
          CodeUri: ./dist/processor.zip


Juniper is responsible for building the artifact for you lambda function based on
the parameters you specify in the manifest file. You can use the generated file
however you wish to. If you choose to use SAM as to define your resources, a basic
development/deployment workflow would be:

    >>> juni build
    >>> sam build
    >>> sam deploy

Using juni along sam is highly recommended. Keep in mind that you can use the
generated artifact to manually update a lambda function from the AWS console.
Or you can also use the AWS cli to update a lambda function:

    >>> aws lambda update-function-code --function-name ProcessorFn --zip-file ./dist/processor.zip

Features
********

Using the available tools in the serverless space, we found there was no tool
capable of fulfilling all of these business needs:

* Minimal manifest file to define packaging
* Using docker containers as a way to install dependencies and generate the artifacts
* Ability to specify a set of requirements.txt per lambda
* Create an individual zip artifact for multiple lambda functions
* Ability to include shared dependencies (python modules relative to the function
  being packaged)

This list defines the entire scope of Juniper.

.. note::

    Keep in mind that Juniper is a packaging tool only! Most of the tools surveyed
    offer a more comprehensive set of features one of which is packaging.


.. _SAM: https://github.com/awslabs/serverless-application-model
.. _AWS Documentation: https://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html


Contents:
=========

.. toctree::
    :maxdepth: 2
    :numbered:
    :glob:

    quickstart.rst
    tutorial.rst
    concepts.rst
    advanced.rst
