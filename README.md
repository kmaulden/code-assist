# Code Assist

`code-assist` is a command-line tool that harnesses OpenAI's code assistance capabilities to enhance existing Python code and generate new code snippets. It offers two main commands: `improve` and `generate`.

## Installation and Execution

The package includes `.whl` files for distribution.

To install the package on your environment, run the following command:
```bash
pip install `_path_to_.whl`
```

Before running, you must ensure that your OpenAI API key is in your environment variables.
```base
OPENAI_API_KEY=your_openai_api_key
```

You can then run the package executable as as below, or optionally set up a `codeassist` alias for this command.
```bash
python {pip install location}/code_assist/cli.py {command}
```

After running each assistant, you may choose to re-use your assistants. You can do this by setting the respective assistant ID's.
```base
OPENAI_CODE_GENERATE_ASSISTANT_ID=code_generate_model_id
OPENAI_CODE_IMPROVE_ASSISTANT_ID=code_improve_model_id
```

## Usage

### Improve
The improve command enhances existing code by taking either (1) copied and pasted code or (2) a file path along with start and end lines as input. Additionally, users can provide specific instructions for code improvement.

All improvement details (i.e. the code input method [copy] or [file], start and end lines if applicable, and instructions) are all defined interactively by the user on the command line.

Run this command with the following
```bash
codeassist improve
```

### Generate
The generate command creates code snippets based on user instructions. Users specify their requirements interactively, and the CLI prompts OpenAI accordingly.

Run this command with the following
```bash
codeassist generate
```

## Author
Kyle Maulden

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
