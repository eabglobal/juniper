#!/usr/bin/env bash

echo "Starting to package $1"

mkdir lambda
pip install -q -t lambda -r $(find common -type f -name requirements.txt)
cp -r common/* lambda/

# Exclude non essential files and folders from the deployment package.
find lambda -type f -name "requirements.txt"   -delete
find lambda -type f -name "manifest.yml"       -delete
find lambda -type f -name "setup.cfg"          -delete
find lambda -type f -name "*.py[co]"           -delete
find lambda -type d -name "__pycache__"        -delete
find lambda -type d -name ".juni"             -exec rm -rf {} +
find lambda -type d -name "tests"              -exec rm -rf {} +
find lambda -type d -name "features"           -exec rm -rf {} +
find lambda -type d -name "*.dist-info*"       -exec rm -rf {} +
find lambda -type d -name "*.egg-info*"        -exec rm -rf {} +

# python -m compileall -q lambda
cd lambda
zip -q -9r "../dist/$1.zip" .

echo 'Finished packaging'