import time

from openai import OpenAI

from code_assist.llm_thread.llm_thread_abstract import LlmThreadAbstract

DEFAULT_NAME_IMRPOVE = "CodeAssistantImprove"
DEFAULT_NAME_GENERATE = "CodeAssistantGenerate"
DEFUALT_MODEL = "gpt-3.5-turbo-0125"
DEFAULT_IMPROVE_INSTRUCTIONS = """
    You are an AI assistant trained to improve Python code.

    When prompted with input code and request instructions, you will respond with
    clear and concise python code that keeps existing functionality, but make the existing
    code more efficient, readable, and Pythonic, while following software developement best practices.

    By default, go ahead and output the improved code at each iteration. No need to wait for the
    users specific instruction to do so.
"""

DEFAULT_GENERATE_INSTRUCTIONS = """
    You are an AI assistant trained to generate Python code.

    When prompted with code requirements, you will generate Python code to acheive the requested result.
    Your code should be efficient, readable, and Pythonic, while following software developement best practices.

    By default, go ahead and output the generated code at each iteration. No need to wait for the
    users specific instruction to do so.
"""


class OpenAiThreadHelper(LlmThreadAbstract):

    def __init__(
        self, api_key, assisant_id, type, code=None, model="gpt-3.5-turbo-0125"
    ):
        self.client = OpenAI(api_key=api_key)
        self.model = model
        self.type = type
        self.assistant_id = assisant_id if assisant_id else self._create_assistant()
        self.thread = self._create_thread()

        if self.type == "improve":
            msg = f"Here is the input code: \n\n{code}"
            self.add_message(msg)

    def _create_thread(self):
        """Creates a thread."""
        return self.client.beta.threads.create()

    def _create_assistant(self, instructions: str = None):
        """Creates an assistant with the default instructions."""
        instructions = instructions or (
            DEFAULT_IMPROVE_INSTRUCTIONS
            if self.type == "improve"
            else DEFAULT_GENERATE_INSTRUCTIONS
        )

        name = DEFAULT_NAME_IMRPOVE if self.type == "improve" else DEFAULT_NAME_GENERATE

        assistant = self.client.beta.assistants.create(
            name=name,
            instructions=instructions,
            tools=[{"type": "code_interpreter"}],
            model=self.model,
        )
        print(f"new assistant created, id#: {assistant.id} \n")
        return assistant.id

    def _check_status(self, run_id):
        """Checks the status of a run every second until it is completed."""

        # TODO implement timeout after max retries, and better handling of all status codes
        run = self.client.beta.threads.runs.retrieve(
            thread_id=self.thread.id, run_id=run_id
        )
        print(f"Current run status: {run.status}")

        while run.status in ["queued", "in_progress"]:
            time.sleep(1)
            run = self.client.beta.threads.runs.retrieve(
                thread_id=self.thread.id, run_id=run_id
            )
            print(f"Current run status: {run.status}")
        return run

    def add_message(self, message) -> None:
        """Adds a message to a thread."""
        self.client.beta.threads.messages.create(
            thread_id=self.thread.id,
            role="user",
            content=message,
        )

    def get_last_message(self) -> str:
        messages = self.client.beta.threads.messages.list(thread_id=self.thread.id)
        messages = [message for message in messages if message.role == "assistant"]
        message = messages[0]
        return f"{message.role}: {message.content[0].text.value}"

    def generate_response(self) -> str:
        """Runs an assistant on a thread."""
        run = self.client.beta.threads.runs.create(
            thread_id=self.thread.id,
            assistant_id=self.assistant_id,
        )
        print(f"Run ID: {run.id}")

        run = self._check_status(run.id)

        return run.status
