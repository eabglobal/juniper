import click
import click_log
import shutil
import logging

from juniper.io import reader
from juniper.constants import DEFAULT_OUT_DIR
from juniper.actions import build_artifacts

logger = logging.getLogger(__name__)
click_log.basic_config(logger)


@click.group()
def main():
    """
    An empty click group, required in order to bundle the other commands.
    """
    pass


@main.command(help="""""")
@click_log.simple_verbosity_option(logger)
def package():
    # TODO: Implement me
    pass


@main.command(help="""""")
@click.option('--manifest', '-m', default='manifest.yml', help='The configuration file to use.')
@click.option('--debug', '-d', is_flag=True, help='Run the build in debug mode.')
@click_log.simple_verbosity_option(logger)
def build(manifest, debug):

    if debug:
        logger.setLevel(logging.DEBUG)

    try:
        manifest_definition = reader(manifest)
        # Make sure to start the building process with a clean slate. This wil
        # ensures that the output folder is not included in the packaging.
        output_dir = manifest_definition.get('package', {}).get('output', DEFAULT_OUT_DIR)
        shutil.rmtree(output_dir, ignore_errors=True)

        build_artifacts(logger, manifest_definition)
    except FileNotFoundError as fe:
        logger.error(f'Unable to find {manifest}.')


if __name__ == '__main__':
    main()
