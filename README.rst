Juniper: Package lambda functions
=================================

|circle| |pypi version| |apache license|

Juniper is a packaging tool to stream and standardize the creation of a zip
artifact for a set of AWS Lambda functions.

The zip artifacts generated include the source code of the dependencies defined
in a given requirements.txt file as well as any shared libraries the function
depends on. With the generated artifact, a developer can deploy a lambda function
either manually, through the awscli or using a cloudformation/sam template.

Quickstart
**********

With Python==3.6 and Docker installed, install juniper:

.. code-block:: text

    > pip install juniper

In order to package your lambda functions with juniper, you need to create a
manifest file.

.. code-block:: yaml

    functions:
      # Name the zip file you want juni to create
      router:
        # The dependencies of the router function.
        requirements: ./src/requirements.txt.
        # Include this file in the generated zip artifact.
        include:
        - ./src/lambda_function.py

The folder structure this manifest refers to looks like:

::

    .
    ├── manifest.yml
    ├── src
    │   ├── requirements.txt
    │   ├── lambda_function.py

Build it!

.. code-block:: text

    > juni build

Juniper creates the following artifact `./dist/router.zip`  🎉

For a more comprehensive example, please take a look at our `tutorial`_.

.. _`tutorial`: https://eabglobal.github.io/juniper/tutorial.html


Python3.7 and Beyond
********************
By default juniper uses docker containers to package your lambda functions. Behind
the scenes, juniper creates a docker-compose file from your manifest. This file is
used by the `build` command to spawn a build container per function definition.

Since the AWS Lambda service supports multiple python runtimes, it makes sense for
juniper to give you the ability to specify a docker image. With the following
manifest file, you can package the router lambda using a python3.7 image.

.. code-block:: yaml

    functions:
      router:
        # Use this docker image
        image: lambci/lambda:build-python3.7
        requirements: ./src/router/requirements.txt.
        # Include these local modules in the artifact
        include:
        - ./src/commonlib/mylib
        - ./src/router_function/router

Keep in mind that not every single docker image works, for more information on
the type of images supported read `juniper and docker`_.

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
