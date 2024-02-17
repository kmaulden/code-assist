import os

import click
import questionary

from code_assist.llm_thread.llm_thread_abstract import LlmThreadAbstract


def _validate_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


def get_input_method():
    result = questionary.select(
        "Would you like to copy & paste the code (copy) or read from file (else)?",
        choices=["copy", "else"],
        default="copy",
    ).ask()

    return result


def get_copied_code():
    code = questionary.text("Paste your code:\n").ask()
    return code


def get_code_from_file():
    # Get the current directory
    current_directory = os.getcwd()

    # Ask the user for the file location within the current directory
    file_location = questionary.path(
        message="Enter file location:", default=current_directory
    ).ask()

    st_line = int(
        questionary.text(
            "What is the start line number (inclusive)?", validate=_validate_integer
        ).ask()
    )

    end_line = int(
        questionary.text(
            "What is the end line number (inclusive)?", validate=_validate_integer
        ).ask()
    )

    file_path = os.path.join(current_directory, file_location)

    with open(file_path, "r") as file:
        all_lines = file.readlines()

    # Ensure that st_line and end_line are within valid range
    st_line = max(st_line, 1)
    end_line = min(end_line, len(all_lines))

    # Filter lines based on st_line and end_line
    selected_lines = all_lines[st_line - 1 : end_line]

    return "".join(selected_lines).rstrip("\n")


def process_thread(ai_helper: LlmThreadAbstract) -> None:

    while True:
        instructions = questionary.text("Instructions: ").ask()
        if (instructions is None) or (instructions.lower() == "exit"):
            break
        else:
            click.echo("Generating response... ")
            ai_helper.add_message(instructions)
            status = ai_helper.generate_response()
            if status == "completed":
                res = ai_helper.get_last_message()
                click.echo(res)
            else:
                click.echo(f"Issue with LLM response - status: {status}. Exiting...")
                break
