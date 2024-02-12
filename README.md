# code-assist
A code assistant cli implementation

## Overview

code-assistant is a command-line tool designed to leverage OpenAI's code assistance capabilities for two main commands: "improve" and "generate."

## Installation

The package uses a poetry virtual environment which contains all required binaries for the package to run.

To install the package on our environment, run the following command:
```bash
hold
```

## Usage

### Improve
The improve command enhances existing code by taking either copied code or a file path along with optional start and end lines as input. Additionally, users can provide specific instructions for code improvement.

The improvement details (i.e. code to be improved and improvement instructions) should be defined interactively by the user on the command line.

### Generate
The generate command creates code snippets based on user instructions. Users interactively specify their requirements, and the CLI will generate code accordingly.
