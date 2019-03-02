from pathlib import Path
from itertools import chain


def validate_manifest_definition(manifest_definition):
    """
    Raise errors if problems are found in the manifest file. It currently
    checks all the include paths exist.
    :param manifest_definition: Dict of the manifest
    """
    if missing_includes(manifest_definition):
        raise FileNotFoundError(f'You have empty include paths: {missing_includes(manifest_definition)}')


def missing_includes(manifest_definition):
    return [path for path in all_includes(manifest_definition)
            if not Path(path).exists()]


def all_includes(manifest_definition):
    return chain.from_iterable(
            function['include']
            for function in manifest_definition['functions'].values())
