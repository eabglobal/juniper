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
    router:                                         # Name of the lambda function (result in router.zip artifact)
        requirements: ./src/router/requirements.txt.  # Path to reqs file
        include:
        - ./src/commonlib/mylib                     # Path for inclusion in code
        - ./src/router_function/router.             # Path for inclusion in code


Build it!

.. code-block:: text

    > juni build

Your .zip is now in the `dist/` directory.  🎉

Features
********

This list defines the entire scope of Juniper. Nothing more, nothing else.

* Minimal manifest file to define packaging
* Using docker containers as a way to install dependencies and generate the artifacts
* Ability to tailor the requirements.txt per lambda
* Create an individual zip artifact for multiple lambda functions
* Ability to include shared dependencies (python modules relative to the function
  being packaged)

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
