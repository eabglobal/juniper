# -*- coding: utf-8 -*-
"""
    test_cli.py
    :copyright: © 2019 by the EAB Tech team.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
        http://www.apache.org/licenses/LICENSE-2.0
    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from unittest.mock import MagicMock
from juniper import cli


logger = MagicMock()


def test_clean_skip_false(mocker):
    """
    Validate that the output directory is deleted from disk.
    Validate that a new output directory is created.
    """

    mock_mkdirs = mocker.patch('os.makedirs')
    mock_rmtree = mocker.patch('shutil.rmtree')

    output_dir_name = 'find/me/NOW'
    manifest = {'output_dir': output_dir_name}

    cli._clean(logger, False, manifest)

    mock_rmtree.assert_called_with(output_dir_name, ignore_errors=True)
    mock_mkdirs.assert_called_with(output_dir_name)


def test_clean_skip_true(mocker):

    mock_mkdirs = mocker.patch('os.makedirs')
    mock_rmtree = mocker.patch('shutil.rmtree')

    output_dir_name = 'find/me/NOW'
    manifest = {'output_dir': output_dir_name}

    cli._clean(logger, True, manifest)

    mock_rmtree.assert_not_called()
    mock_mkdirs.assert_called_with(output_dir_name, exist_ok=True)
