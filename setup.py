from setuptools import setup, find_packages


setup(
    name="juniper",
    version='0.1',
    description='',
    author='EAB Tech',
    author_email='eabtech@eab.com',
    packages=find_packages(),
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
