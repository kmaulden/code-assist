import click

from code_assist.utils import get_code_from_file, get_copied_code, get_input_method, process_thread
from code_assist.llm_thread.openai_thread import OpenAiThreadHelper

@click.group()
def cli():
    pass


@cli.command()
def generate():
    """Generate new code."""
    click.echo("Not yet implemented!")


@cli.command()
def improve():
    """Improve existing code."""
    input_method = get_input_method()

    if input_method == "copy":
        # request and process copied code
        code = get_copied_code()
    else:
        # request and process file location
        code = get_code_from_file()
    click.echo(code)
    
    # TODO put key in env
    ai_helper = OpenAiThreadHelper("", 'improve', code)
    process_thread(ai_helper=ai_helper)


if __name__ == "__main__":
    cli()
