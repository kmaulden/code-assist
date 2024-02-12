from openai import OpenAI

from code_assist.llm_thread.llm_thread_abstract import LlmThreadAbstract


class OpenAiThread(LlmThreadAbstract):

    def __init__(self, api_key, model = "gpt-3.5-turbo"):
        self.client = OpenAI(api_key=api_key)
        self.model = model

    def _create_thread(self):
        pass

    def _check_status(self):
        pass

    def add_message(self, message) -> str:
        pass

    def generate_response(self):
        pass

    

        