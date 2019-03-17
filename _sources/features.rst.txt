Features
========
By default juniper builds a docker-compose file from the manifest definition. This
file will then be used to build the .zip artifacts. When using the vanilla version
of the `juni build` command, you need to be aware of the following defaults:

* Docker will always be used as the default packaging medium
* DEFAULT_DOCKER_IMAGE = 'lambci/lambda:build-python3.6'
* The output directory is *./dist*
* The output directory will be recreated on every build every single time

Custom Docker Image
*******************
To build the lambda artifacts, by default, juniper will use a python3.6 docker image.
Given that AWS lambda supports multiple runtimes, juniper gives the developer the
option to specify the docker image to use for build purposes.

To build an artifact with a different version of the runtime, as a developer you
need to add the image attribute to your manifest. Juniper supports the image definition
at a global level and at a function level.

The image override specified at a global level applies to every single function
in the manifest.

.. code-block:: yaml

    global:
        image: lambci/lambda:build-python3.7

    functions:

      router:
        requirements: ./router/requirements.txt.
        include:
            - ./commonlib/common
            - ./router_function/router

If you have multiple function definitions in the manifest file, you can also
specify the docker image at the function level. Keep in mind that the function
level override has precedence over the global definition. Which means that you can
specify a docker image at a global level, and also specify a particular version
of python for a given function.

.. code-block:: yaml

    global:
        image: lambci/lambda:build-python3.7

    functions:

      router:
        requirements: ./router/requirements.txt.
        include:
            - ./commonlib/common
            - ./router_function/router

      legacy: # Name of the lambda function
        image: lambci/lambda:build-python2.7
        requirements: ./legacy/requirements.txt.
        include:
            - ./commonlib/common
            - ./legacy_function/legacy

In this particular example the router function will be packaged using the python3.7
docker image and the legacy function will be packaged using python 2.7.

Recommended docker images
*************************

We highly recommend using the lambci_ **lambci/lambda:build-python** images. These images
are guaranteed to work for the runtimes supported by AWS lambda functions. The
usage of these images is recommended, because they "include packages like gcc-c++,
git, zip and the aws-cli for compiling and deploying."

* lambci/lambda:build-python2.7
* lambci/lambda:build-python3.6
* lambci/lambda:build-python3.7

.. _lambci: https://github.com/lambci/docker-lambda