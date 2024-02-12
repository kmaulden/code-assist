import abc

class LlmThreadAbstract(metaclass=abc.ABCMeta):
    """
    LLM Thread Abstract class
    """

    @abc.abstractmethod
    def add_message(self, message):
        pass

    @abc.abstractmethod
    def generate_response(self, message):
        pass
