import io
import re
from collections import OrderedDict
from setuptools import setup, find_packages


with io.open('README.rst', 'rt', encoding='utf8') as f:
    readme = f.read()

# Make sure that the version of the package always matches the version of the
# tool. The version of the __init__.py is updated with the make release command.
with io.open('juniper/__init__.py', 'rt', encoding='utf8') as f:
    version = re.search(r'__version__ = \'(.*?)\'', f.read()).group(1)

setup(
    name="juniper-aidentified",
    version=version,
    author='Aidentified LLC',
    author_email='dgilman@aidentified.com',
    description="Tool to streamline the build of python lambda functions. (fork of juniper)",
    long_description=readme,
    project_urls=OrderedDict((
        ('Code', 'https://github.com/dgilmanAIDENTIFIED/juniper'),
    )),
    license='Apache Software License',
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    entry_points={
        'console_scripts': ['juni=juniper.cli:main'],
    },
    python_requires='>=3.6',
    test_suite="tests",
    install_requires=[
        'click>=8.0',
        'click-log',
        'PyYAML>=6.0',
        'Jinja2>=3.0',
    ],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Build Tools',
    ])
