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
    name="juniper",
    version=version,
    author='EAB Tech',
    author_email='eabtech@eab.com',
    description="Tool to streamline the build of python lambda functions.",
    long_description=readme,
    project_urls=OrderedDict((
        ('Documentation', 'https://eabglobal.github.io/juniper/'),
        ('Code', 'https://github.com/eabglobal/juniper'),
        ('Issue tracker', 'https://github.com/eabglobal/juniper/issues'),
    )),
    license='Apache Software License',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': ['juni=juniper.cli:main'],
    },
    python_requires='>=3.6',
    test_suite="tests",
    install_requires=[
        'click>=5.1',
        'click-log',
        'PyYAML >= 3.10, < 4.3',
        'Jinja2>=2.10',
        'docker-compose>=1.20, < 1.24'
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
