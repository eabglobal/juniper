#!/usr/bin/env bash

echo "Starting to build $1 layer"

mkdir layer
# Requirements file specified in the manifest will ALWAYS be in this path!
requirements="common/requirements.txt"

if [ ! -f $requirements ]; then
    echo "Unable To Build layer - A path to the requirements file is needed."
    exit 1
fi

pip install -q -t layer -r ${requirements}
cp -r common/* layer/

# Exclude non essential files and folders from the deployment package.
find layer -type f -name "requirements.txt"   -delete
find layer -type f -name "manifest.yml"       -delete
find layer -type f -name "setup.cfg"          -delete
find layer -type f -name "*.py[co]"           -delete
find layer -type d -name "__pycache__"        -delete
find layer -type d -name ".juni"             -exec rm -rf {} +
find layer -type d -name "tests"              -exec rm -rf {} +
find layer -type d -name "features"           -exec rm -rf {} +
find layer -type d -name "*.dist-info*"       -exec rm -rf {} +
find layer -type d -name "*.egg-info*"        -exec rm -rf {} +

# python -m compileall -q lambda
mv layer ./dist/$1_layer
echo 'Finished making layer'