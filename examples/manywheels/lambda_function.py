import xmlsec
from lxml import etree


# https://stackoverflow.com/questions/55508626/lambda-not-loading-cryptography-shared-library
# https://gist.github.com/vladgolubev/439559fc7597a4fb51eaa9e97b72f319
def lambda_handler(event, context):
    manager = xmlsec.KeysManager()

    return {'hello': 'world'}
