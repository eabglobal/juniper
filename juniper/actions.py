# -*- coding: utf-8 -*-
"""
    actions.py
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

import os
import shutil
import subprocess
from juniper.constants import DEFAULT_OUT_DIR, DEFAULT_DOCKER_IMAGE
from juniper.io import (get_artifact, write_tmp_file, get_artifact_path)


def build_artifacts(logger, manifest):
    """
    Creates a .zip file for each one of the serverless functions defined in the given
    manifest definitions file. Each function must include a name, and the set of directories
    to be included in the artifact. As part of the packaging, if the given function
    has a definition of a requirements file, all the dependencies in that file will be
    included in the artifact.

    :param logger: The logger instance.
    :param manifest: The definition of the functions and global parameters as defined in the input file.
    """

    compose_fn = build_compose(logger, manifest)
    logger.debug(f'docker-compose.yml - {compose_fn}')
    try:
        # Must copy the bin directory to the client's folder structure. This directory
        # will be promtly cleaned up after the artifacts are built.
        os.makedirs('./.juni/bin', exist_ok=True)
        shutil.copy(get_artifact_path('package.sh'), './.juni/bin/')

        # Use docker as a way to pip install dependencies, and copy the business logic
        # specified in the function definitions.
        subprocess.run(["docker-compose", "-f", compose_fn, '--project-directory', '.', 'down'])
        subprocess.run(["docker-compose", "-f", compose_fn, '--project-directory', '.', 'up'])
    finally:
        shutil.rmtree('./.juni', ignore_errors=True)


def build_compose(logger, manifest):
    """
    Builds a docker-compose file with the lambda functions defined in the manifest.
    The definition of the lambda functions includes the name of the function as
    well as the set of dependencies to include in the packaging.

    :param logger: The logger instance.
    :param manifest: The yaml file that contains the info of the functions to package.
    """

    compose = '\n'.join([_get_compose_header(manifest), _get_compose_sections(manifest)])

    # Returns the name of the temp file that has the docker-compose definition.
    return write_tmp_file(compose)


def _get_compose_header(manifest):
    """
    Returns the static docker-compose header. Used when building the compose file.
    """
    return get_artifact('compose_header.yml')


def _get_compose_sections(manifest):
    """
    Build the service entry for each one of the functions in the given context.
    Each docker-compose entry will depend on the same image and it's just a static
    definition that gets built from a template. The template is in the artifacts
    folder.
    """

    template = get_artifact('compose_entry.yml')

    sections = [
        _build_compose_section(manifest, template, name, definition)
        for name, definition in manifest.get('functions', {}).items()
    ]

    return '\n\n'.join(sections)


def _build_compose_section(manifest, template, name, sls_function):
    """
    Builds a single docker-compose entry for a given serverless function. Includes
    the volumes mapping as well as the basic info of the function. Also, if the
    function has a given requirements file definition, the file will be included
    as part of the volumes mapping.

    :param template: The static template that defines the docker compose entry for the function
    :param name: The name of the serverless function
    :param sls_function: The actual object with the parameters needed to stamp the template
    """

    def get_vol(include):
        name = include[include.rindex('/') + 1:]
        return f'      - {include}:/var/task/common/{name}'

    output_dir = manifest.get('package', {}).get('output', DEFAULT_OUT_DIR)
    volumes = [
        f'      - {output_dir}:/var/task/dist',
        '      - ./.juni/bin:/var/task/bin',
    ] + [
        get_vol(include)
        for include in sls_function.get('include', [])
    ]

    reqs_path = sls_function.get('requirements')
    if reqs_path:
        volumes.append(f'      - {reqs_path}:/var/task/common/requirements.txt')

    return template.format(
        name=name,
        docker_image=_get_docker_image(manifest, sls_function),
        volumes='\n'.join(volumes))


def _get_docker_image(manifest, sls_function):
    """
    Get the docker image that will be used to package a given function. Precedence
    is as follows: function level override, global image override, default.

    :params manfiest: The juniper manifest file.
    :params sls_function: The serverless function definition.
    """

    function_image = sls_function.get('image')
    if function_image:
        return function_image

    global_image = manifest.get('global', {}).get('image')
    if global_image:
        return global_image

    return DEFAULT_DOCKER_IMAGE
