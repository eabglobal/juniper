# Juniper: Tool to package lambda functions

Packaging of python lambda functions is a problem a web developer faces when
building web APIs using AWS services. The main issue is that the dependencies
of the function must be included along with the business logic of the function.

This is a minimal implementation of a packaging tool created with a single
purpose in mind: build a .zip artifact for a set of lambda functions.

This tool does not deploy or update a lambda function in AWS. This
tool is used to generate a set of .zip files contaning dependencies and
shared libraries, which you can use to deploy a lambda function.

# Quickstart

With Python==3.6 and Docker installed, install juniper:

    >>> git clone git@github.com:eabglobal/juniper.git
    >>> cd juniper
    >>> pip install -e .

Go to the code you are packaging and define a configuration for your
functions, ex in `manifest.yml`:

```yaml
functions:
  router:                                         # Name of the lambda function (result in router.zip artifact)
    requirements: ./src/router/requirements.txt.  # Path to reqs file
    include:
      - ./src/commonlib/mylib                     # Path for inclusion in code
      - ./src/router_function/router.             # Path for inclusion in code
```

Build it!

    >>> juni build

Your .zip is now in the `dist/` directory.  🎉

Contributing
------------

For guidance on setting up a development environment and how to make a
contribution to Juniper, see the `contributing guidelines`_.

.. _contributing guidelines: https://github.com/eabglobal/juniper/blob/master/CONTRIBUTING.rst

Links
-----

* Documentation: https://eabglobal.github.io/juniper/
* License: `BSD <https://github.com/eabglobal/juniper/blob/master/LICENSE>`_
* Code: https://github.com/eabglobal/juniper
* Issue tracker: https://github.com/eabglobal/juniper/issues
* Test status:

  * Linux, Mac: https://circleci.com/gh/eabglobal/juniper
