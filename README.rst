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
        requirements: ./src/requirements.txt
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

The juni build command will generate the lambda artifact for all the functions and
layers defined in the manifest file. However, during the development process, it may be
desired to only build the lambda functions that a developer is actively working on.

To build only a subset of the resources defined in the manifest use the following
command:

.. code-block:: text

    > juni build --skip-clean -f <target_fn_name>

This command will build all the functions that partially match the given target_fn_name.
When using a naming convention a developer has the ability to build a subset of
the lambdas defined in the manifest.

The skip-clean flag will prevent the previously built artifacts from being deleted
before the build is executed.

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
        requirements: ./src/router/requirements.txt
        # Include these local modules in the artifact
        include:
        - ./src/commonlib/mylib
        - ./src/router_function/router

Keep in mind that not every single docker image works, for more information on
the type of images supported read `juniper and docker`_.

.. _`juniper and docker`: https://eabglobal.github.io/juniper/features.html

Lambda Layers
*************
AWS Lambda layers is a recent service that gives a developer the ability to
pre-package a set of dependencies. A lambda function can be built on top of multiple
layers, either packaged by the developer, by AWS or by a third party.

To build a layer, the juniper manifest uses a new block:

.. code-block:: yaml

  layers:
    base:
      requirements: ./src/requirements/base.txt
    pg:
      requirements: ./src/requirements/postgres.txt

With this manifest, running **juni build** creates two layer artifacts: one with the
name base and another one named pg. Lambda layers are packaged along the lambda
functions defined in the manifest and the zip files are stored in the artifacts directory.

The generated artifact includes the dependencies defined in the requirements file
of the lambda layer.

Each individual section supports the definition of a custom docker image. With this
feature, a layer can be built using python3.7 and another one can be built using the
default python interpreter; python3.6.

.. code-block:: yaml

  layers:
    base:
      image: lambci/lambda:build-python3.7
      requirements: ./src/requirements/base.txt


Juniper builds the artifact for you, you can either use the `layers aws cli`_ to
upload it to AWS or you can use a SAM template definition. While using a SAM template,
make sure you use the `AWS::Serverless::LayerVersion` resource.

To see an example on how to package lambda functions with layers, juniper includes
an example in the codebase called `ridge`_.

.. _`layers aws cli`: https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html#configuration-layers-manage
.. _`ridge`: https://github.com/eabglobal/juniper/tree/master/examples/ridge

Configuration
*************
To update the default configuration of juniper, can use the the global section
of the manifest. A sample configuration looks like:

.. code-block:: yaml

    global:
      image: lambci/lambda:build-python3.7
      output: ./build

    functions:
      router:
        requirements: ./src/router/requirements.txt
        include:
        - ./src/router_function/router/lambda_function.py

Setting a docker image at a global level tells juniper to package every
lambda function using that image. In this example, the zip artifacts will be stored in
the ./build folder instead of the ./dist; which is the default.

Include Binaries
****************
Using the lambci build images to create the zip artifacts for a given set of lambda
functions is sufficient for most use cases. However, there are times when the base container
does not have all the build libraries necessary to install a python package. In this cases
running `juni build` fails while trying to pip install the dependencies of the function.
In addition, once the libraries are installed in the container some packages require a set of
binaries to work properly at runtime.

The recommended procedure to install OS libraries and include missing dependencies
is to use a dockerfile to build a local docker image. The strategy is illustrated as follows:

* Create a dockerfile using one of the lambci images as a starting point
* Build a local docker image from the docker file
* Use the local image in the juniper manifest

With this startegy, the juniper manifest will look like this:

.. code-block:: yaml

    functions:
      router:
        image: custom/local_docker_image
        requirements: ./src/router/requirements.txt
        include:
        - ./src/router_function/router/lambda_function.py

In this case, a developer needs to build the docker image before executing the
juni build command.

At this point, the developer can push the docker image to the docker hub and use
the hosted version instead of the local one. This strategy separates the build of
a custom image from the build of the artifacts.

If you need binaries in the final artifact, you can place these files either in the
**/var/task/lambda_lib/** or the **/var/task/lambda_bin/** depending on your use case.
Files added to the bin folder are included in the PATH, files added to the lib,
are included in the LD_LIBRARY_PATH. For more information view `aws layer config`_.

Juniper is in charge of putting the files in the lambda_bin and lambda_lib in
the right place when building an artifact.

A concrete example of the configuration is outlined in the `advanced`_ section
of our documentation.

.. _`advanced`: https://eabglobal.github.io/juniper/advanced.html
.. _`aws layer config`: https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html#configuration-layers-path

PIP Configuration
*****************
To set any pip configuration parameters, create a pip.conf file and add the path
to the manifest. The **pipconf** setting is only available at a global level and
it will apply to the packaging of all the functions defined in the manifest.

.. code-block:: yaml

  global:
    pipconf: ./pip.conf

  functions:
    sample:
      requirements: ./requirements.txt
      include:
        - ./lambda_function.py

A sample pip.conf file can be seen bellow, to see the entire list of parameters
visit the official `pip documentation`_.

.. code-block:: yaml

  [global]
  timeout = 5
  index-url = https://download.zope.org/ppix

.. _`pip documentation`: https://pip.pypa.io/en/stable/user_guide/#config-file

Features
********

This list defines the entire scope of Juniper. Nothing more, nothing else.

* Minimal manifest file to define packaging
* Using docker containers as a way to install dependencies and generate the artifacts
* Ability to tailor the requirements.txt per lambda
* Create an individual zip artifact for multiple lambda functions
* Ability to include shared dependencies (python modules relative to the function
  being packaged)
* Specify docker image to package lamdba functions using different python runtimes
* Define pip command line arguments using a pip.conf file
* Packaging of lambda layers

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
