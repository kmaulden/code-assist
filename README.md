# Code Assist

`code-assist` is a command-line tool that harnesses OpenAI's code assistance capabilities to enhance existing Python code and generate new code snippets. It offers two main commands: `improve` and `generate`.

## Installation

The package uses a poetry virtual environment which contains all required binaries for the package to run.

To install the package on our environment, run the following command:
```bash
hold
```

You must ensure that your OpenAI API key is in your environment variables.
   ```base
   OPENAI_API_KEY=your_openai_api_key
   OPENAI_CODE_GENERATE_ASSISTANT_ID=code_generate_model_id
   OPENAI_CODE_IMPROVE_ASSISTANT_ID=code_improve_model_id
   ```

After running each assistant, you may choose to re-use your assistants. You can do this by setting the respective assistant ID's.

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

# OpenAI Assistant CLI

This CLI tool allows you to generate and improve code using OpenAI's code generation models.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your OpenAI API key in a .env file:
   ```plaintext
   OPENAI_API_KEY=your_openai_api_key
   OPENAI_CODE_GENERATE_ASSISTANT_ID=code_generate_model_id
   OPENAI_CODE_IMPROVE_ASSISTANT_ID=code_improve_model_id
   ```


## Author
Kyle Maulden

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
