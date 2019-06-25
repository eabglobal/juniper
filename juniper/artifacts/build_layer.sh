#!/usr/bin/env bash

echo "Starting to build $1 layer"

mkdir -p lambda_lib
mkdir -p layer/python layer/lib

# Requirements file specified in the manifest will ALWAYS be in this path!
requirements="common/requirements.txt"

if [ ! -f $requirements ]; then
    echo "Unable To Build layer - A path to the requirements file is needed."
    exit 1
fi

pip install -q -t layer/python -r ${requirements}
cp -r common/* layer/python/

if [ "$(ls -A lambda_lib)" ]; then
    # All – bin (PATH), lib (LD_LIBRARY_PATH)
    # https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html#configuration-layers-path
    cp -r lambda_lib/* layer/lib/
fi

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