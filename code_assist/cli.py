import click
import os
from code_assist.utils import get_input_method, get_copied_code, get_code_from_file

@click.group()
def cli():
    pass

@cli.command()
def generate():
    """Generate new code."""
    click.echo('Not yet implemented!')

@cli.command()
def improve():
    """Improve existing code."""
    click.echo('Not yet implemented!')

    input_method = get_input_method()

    if input_method == "copy":
        # request and process copied code
        code = get_copied_code()
    else:
        # request and process file location
        code = get_code_from_file()

    click.echo(code)




if __name__ == '__main__':
    cli()