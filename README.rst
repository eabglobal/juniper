Juniper: Package lambda functions
=================================

|circle| |pypi version| |apache license|

Juniper is a packaging tool with a with a single purpose in mind: stream and standardize
the creation of a zip artifact for a set of AWS Lambda functions.

Packaging of python lambda functions is a problem a web developer faces when
building web APIs using AWS services. The main issue is that the dependencies
of the function must be included along with the business logic of the function.

This tool does **not** deploy or update a lambda function in AWS. This
tool is used to generate a set of .zip files contaning dependencies and
shared libraries, which you can use to deploy a lambda function.

Quickstart
**********

With Python==3.6 and Docker installed, install juniper:

.. code-block:: text

    > pip install juniper

Go to the code you are packaging and define a configuration for your
functions, ex in `manifest.yml`:

.. code-block:: yaml

    functions:
      # Name of the lambda function (result in router.zip artifact)
      router:
        requirements: ./src/requirements.txt.
        # Include these packages in the artifact.
        include:
        - ./src/lambda_function.py

The folder structure this manifest refers to looks like:

```
~/ tree
.
├── manifest.yml
├── src
│   ├── requirements.txt
│   ├── lambda_function.py
```

Build it!

.. code-block:: text

    > juni build

Your .zip is now in the `./dist` directory.  🎉

Python3.7 and Beyond
********************
By default juniper uses docker containers to package your lambda functions. Behind
the scenes, juniper creates a docker-compose file from your manifest and from that
file it spawns a set of containers to create the zip files.

Since the AWS Lambda service supports multiple python runtimes, it makes sense for
juniper to give you the ability to specify a docker image. With the following
manifest file, you can package the router lambda using a python3.7 image.

.. code-block:: yaml

    functions:
      router:
        # Use this docker image
        image: lambci/lambda:build-python3.7
        requirements: ./src/router/requirements.txt.
        include:
        - ./src/commonlib/mylib
        - ./src/router_function/router.

Keep in mind that not every single docker image works, for more information on
the type of images supported read `juniper and docker`_

.. _`juniper and docker`: https://eabglobal.github.io/juniper/features.html

Features
********

This list defines the entire scope of Juniper. Nothing more, nothing else.

* Minimal manifest file to define packaging
* Using docker containers as a way to install dependencies and generate the artifacts
* Ability to tailor the requirements.txt per lambda
* Create an individual zip artifact for multiple lambda functions
* Ability to include shared dependencies (python modules relative to the function
  being packaged)
* Specify docker image to package lamdba functions using different python runtimes.

Contributing
************

For guidance on setting up a development environment and how to make a
contribution to Juniper, see the `contributing guidelines`_.

.. _contributing guidelines: https://github.com/eabglobal/juniper/blob/master/CONTRIBUTING.rst

Links
*****

* Documentation: https://eabglobal.github.io/juniper/
* License: `Apache Software License`_

* Code: https://github.com/eabglobal/juniper
* Issue tracker: https://github.com/eabglobal/juniper/issues
* Test status:

  * Linux, Mac: https://circleci.com/gh/eabglobal/juniper

.. _Apache Software License: https://github.com/eabglobal/juniper/blob/master/LICENSE


.. |circle| image:: https://circleci.com/gh/eabglobal/juniper/tree/master.svg?style=shield
    :target: https://circleci.com/gh/eabglobal/juniper/tree/master

.. |pypi version| image:: https://img.shields.io/pypi/v/juniper.svg
    :target: https://pypi.org/project/juniper/

.. |apache license| image:: https://img.shields.io/github/license/eabglobal/juniper.svg
    :target: https://github.com/eabglobal/juniper/blob/master/LICENSE
