from setuptools import setup, find_packages


with open("README.rst", "r") as fh:
    long_description = fh.read()


setup(
    name="juniper",
    version='0.1.0',
    description='',
    author='EAB Tech',
    author_email='eabtech@eab.com',
    description="Tool to streamline the build of python lambda functions."
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': ['juni=juniper.cli:main'],
    },
    python_requires='>=3.4',
    test_suite="tests",
    install_requires=[
        'click', 'click-log', 'PyYAML'
    ],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"])
