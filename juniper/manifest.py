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
    return [f for f in all_keys(manifest_definition, key)
            if not Path(f).exists()]


def all_keys(manifest_definition, key):
    result = [function[key] for function in manifest_definition['functions'].values()]
    return result if isinstance(result[0], str) else chain.from_iterable(result)
