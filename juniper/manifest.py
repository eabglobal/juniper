from pathlib import Path
from itertools import chain


def validate_manifest_definition(manifest_definition):
    """
    Raise errors if problems are found in the manifest file. It checks if
    requirements and include paths exist.
    :param manifest_definition: Dictionary of the manifest
    """
    if missing('requirements', manifest_definition):
        raise FileNotFoundError('You have missing requirements files: '
                                f'{missing("requirements", manifest_definition)}')
    if missing('include', manifest_definition):
        raise FileNotFoundError('You have empty include paths: '
                                f'{missing("include", manifest_definition)}')


def missing(key, manifest_definition):
    """
    Return all file paths from the key of the manifest that don't exist.
    :param key: A key in the manifest_definitions functions dictionary
    :param manifest_definition: Dictionary of the manifest
    :return: Dictionary of all paths or files that don't exist
    """
    return [f for f in all_keys(manifest_definition, key)
            if not Path(f).exists()]


def all_keys(manifest_definition, key):
    """
    Return all file paths from the key of the manifest.
    :param manifest_definition: Dictionary of the manifest
    :param key: A key in the manifest_definitions functions dictionary
    :return: All paths specified for that key in the manifest file
    """
    result = [function[key] for function in manifest_definition['functions'].values()]
    return result if isinstance(result[0], str) else chain.from_iterable(result)
