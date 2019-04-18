#!/usr/bin/env bash

echo "Starting to build $1 layer"

mkdir -p layer/python
# Requirements file specified in the manifest will ALWAYS be in this path!
requirements="common/requirements.txt"

if [ ! -f $requirements ]; then
    echo "Unable To Build layer - A path to the requirements file is needed."
    exit 1
fi

pip install -q -t layer/python -r ${requirements}
cp -r common/* layer/python/

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


cd layer
zip -q -9r "../dist/$1.zip" .
echo 'Finished making layer'