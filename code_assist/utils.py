import os
import questionary

def _validate_integer(value):
    try:
        int_value = int(value)
        return True
    except ValueError:
        return False

def get_input_method():
    result = questionary.select(
        "Would you like to copy & paste the code (copy) or read from file (else)?",
        choices=["copy", "else"],
        default="copy"
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
        message="Enter file location:",
        default=current_directory
    ).ask()

    st_line = int(questionary.text(
        "What is the start line number (inclusive)?",
        validate=_validate_integer
    ).ask())

    end_line = int(questionary.text(
        "What is the end line number (inclusive)?",
        validate=_validate_integer
    ).ask())

    file_path = os.path.join(current_directory, file_location)

    with open(file_path, 'r') as file:
        all_lines = file.readlines()

    # Ensure that st_line and end_line are within valid range
    st_line = max(st_line, 1)
    end_line = min(end_line, len(all_lines))

    # Filter lines based on st_line and end_line
    selected_lines = all_lines[st_line - 1:end_line]

    return ''.join(selected_lines).rstrip("\n")
