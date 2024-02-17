import os

import click
from dotenv import load_dotenv

from code_assist.llm_thread.openai_thread import OpenAiThreadHelper
from code_assist.utils import (
    get_code_from_file,
    get_copied_code,
    get_input_method,
    process_thread,
)

load_dotenv()


@click.group()
def cli():
    pass


@cli.command()
def generate():
    """Generate new code."""
    ai_helper = OpenAiThreadHelper(
        os.environ.get("OPENAI_API_KEY"),
        os.environ.get("OPENAI_CODE_GENERATE_ASSISTANT_ID"),
        "generate",
    )

    process_thread(ai_helper=ai_helper)


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

    ai_helper = OpenAiThreadHelper(
        os.environ.get("OPENAI_API_KEY"),
        os.environ.get("OPENAI_CODE_IMPROVE_ASSISTANT_ID"),
        "improve",
        code,
    )

    process_thread(ai_helper=ai_helper)


if __name__ == "__main__":
    cli()
