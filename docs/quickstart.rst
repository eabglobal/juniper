.. _quickstart

Quickstart
==========

.. image:: https://farm5.staticflickr.com/4259/35163667010_8bfcaef274_k_d.jpg

Eager to get started? This page gives a good introduction on how to start
packaging your lambda functions with juniper.

Dependencies
************
Juniper supports Python 3.4 and newer only. We recommend using the latest version of Python 3.

`Docker`_ used as the dependable medium to generate the zip files of your lambda functions.

`docker-compose`_ behind the scenes juniper creates a docker-compose file from your
manifest. This file will be used to package your lambda functions. Usind compose,
allows juniper to build your packages in parallel and using a known docker image
you are guarantee the same results independent of your local configuration.

.. _Docker: https://docs.docker.com/docker-for-mac/install/
.. _docker-compose: https://docs.docker.com/compose/install/

Installation
************

Start by creating a brand new virtual environment for the project. You can create
the virtualenv either inside your project's folder or outside. Use the following
commands:

    >>> python3 -m venv venv
    >>> source venv/bin/activate

After activating your virtual environment, install Juniper.

    >>> pip install git+https://github.com/eabglobal/juniper.git

That's it, with juniper installed, you're ready to start packaging your python
lambda functions.

Package Lambdas
***************

To build a set of lambda functions, you need to give juniper a manifest file. In its
most basic form a `manifest.yml` looks like:

.. code-block:: yaml

    functions:

      router: # Name of the lambda function
        requirements: ./router/requirements.txt.
        include:
            - ./commonlib/common          # Include this module
            - ./router_function/router    # Include this module

After you run:

    >>> juni build

The command will create: ./dist/router.zip

Profit!!

So what did just happen?
************************

Let's break the manifest file line by line to understand how juniper uses it in
order to make the zip file.

1. functions: this block lets juniper know that you're about to define a set
  of lambda functions that need to be packaged individually.

2. router: The name of the lambda function. This value will be used as the name
  of the generated zip file.

3. requirements: The python dependencies of the given function. Juniper will include
  all the dependencies specified in this file in the artifact.

4. include: The line items in the following section define the contents of the zip
  file. This block must list the business logic of the lambda function as well as
  any local packages to include.

Given a file definition like the one above, juniper creates a zip artifact
for **every** single function under the functions block.

By default the `build` command will look for a file called `manifest.yml`, if it
finds it, it will generate the artifacts. The artifacts generated will be stored
in the `./dist` directory.

That's it!
