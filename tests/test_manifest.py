import pytest

from juniper.manifest import validate_manifest_definition


def test_source_in_manifest_does_not_exist_notifies_dev():
    manifest_definition = {'package': {'output': './build'},
                           'functions': {'sample': {'requirements': './requirements/dev.txt',
                                                    'include': ['./']},
                                         'another': {'requirements': './requirements/dev.txt',
                                                     'include': ['./idontexist']}}}

    with pytest.raises(FileNotFoundError) as e:
        validate_manifest_definition(manifest_definition)

    assert str(e.value) == "You have empty include paths: ['./idontexist']"


def test_requirements_in_manifest_does_not_exist_notifies_dev():
    manifest_definition = {'package': {'output': './build'},
                           'functions': {'sample': {'requirements': './idontexist.txt',
                                                    'include': ['./']},
                                         'another': {'requirements': './requirements/dev.txt',
                                                     'include': ['./']}}}

    with pytest.raises(FileNotFoundError) as e:
        validate_manifest_definition(manifest_definition)

    assert str(e.value) == "You have missing requirements files: ['./idontexist.txt']"
