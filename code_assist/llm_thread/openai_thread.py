import time

from openai import OpenAI

from code_assist.llm_thread.llm_thread_abstract import LlmThreadAbstract


class OpenAiThread(LlmThreadAbstract):

    def __init__(self, api_key, model = "gpt-3.5-turbo"):
        self.client = OpenAI(api_key=api_key)
        self.thread = self._create_thread()
        self.assistant = self._create_assistant()

    def _create_thread(self):
        """Creates a thread."""
        return self.client.beta.threads.create()

    def _create_assistant(self, name: str, default_instructions: str, model: str):
        """Creates an assistant with the default instructions."""
        assistant = self.client.beta.assistants.create(
            name=name,
            instructions=default_instructions,
            tools=[{"type": "code_interpreter"}],
            model=model,
        )
        print(f"new assistant created, id#: {assistant.id} \n")
        return assistant

    def _check_status(self, run_id):
        """Checks the status of a run every second until it is completed."""

        # todo implement timeout after max retries, and better handling of all status codes
        run = self.client.beta.threads.runs.retrieve(thread_id=self.thread.id, run_id=run_id)
        print(f"Current run status: {run.status}")

        while run.status in ["queued", "in_progress"]:
            time.sleep(1)
            run = self.client.beta.threads.runs.retrieve(thread_id=self.thread.id, run_id=run_id)
            print(f"Current run status: {run.status}")
            
    def add_message(self, message) -> str:
        """Adds a message to a thread."""
        self.client.beta.threads.messages.create(
            thread_id=self.thread.id,
            role="user",
            content=message,
        )

    def _print_last_message(self):
        messages = self.client.beta.threads.messages.list(thread_id=self.thread.id)
        messages = [message for message in messages if message.role == "assistant"]
        message = messages[0]
        print(f"{message.role}: {message.content[0].text.value}")

    def generate_response(self, instructions: str):
        """Runs an assistant on a thread."""
        run = self.client.beta.threads.runs.create(
            thread_id=self.thread.id,
            assistant_id=self.assistant.id,
            instructions=instructions,
        )
        print(f"Run ID: {run.id}")
        
        run = self._check_status(run.id)

        if run.status == 'completed':
            self._print_last_message()
        else:
            print(f"Issue with run! Status is {run.status}")
        
        return run


    

        