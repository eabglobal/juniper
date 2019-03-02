import click
import click_log
import shutil
import logging

from juniper.io import reader
from juniper.constants import DEFAULT_OUT_DIR
from juniper.actions import build_artifacts
from juniper.manifest import validate_manifest_definition


logger = logging.getLogger(__name__)
click_log.basic_config(logger)


@click.group()
def main():
    """
    Juniper is a packaging tool with a with a single purpose in mind:
    stream and standardize the creation of a zip artifact for a set of
    AWS lambda functions.
    """
    pass


# @main.command(help="""""")
# @click_log.simple_verbosity_option(logger)
# def package():
#     # TODO: Implement me
#     pass


@main.command(help="""Packages a set of lambda functions defined in a given manifest file.
                      The manifest must defined these parameters:
                      1 - The name of each function to package
                      2 - A clear path to the dependencies of each lambda function
                      3 - The actual codebase to include in each zip file
                    """)
@click.option('--manifest', '-m', default='manifest.yml', help='The configuration file to use.')
@click.option('--debug', '-d', is_flag=True, help='Run the build in debug mode.')
@click_log.simple_verbosity_option(logger)
def build(manifest, debug):

    if debug:
        logger.setLevel(logging.DEBUG)

    try:
        manifest_definition = reader(manifest)
        validate_manifest_definition(manifest_definition)
    except FileNotFoundError as fnf:
        logger.error(str(fnf))
    else:
        # Make sure to start the building process with a clean slate. This will
        # ensures that the output folder is not included in the packaging.
        output_dir = manifest_definition.get('package', {}).get('output', DEFAULT_OUT_DIR)
        shutil.rmtree(output_dir, ignore_errors=True)

        build_artifacts(logger, manifest_definition)


if __name__ == '__main__':
    main()
