import abc


class LlmThreadAbstract(metaclass=abc.ABCMeta):
    """
    LLM Thread Abstract class
    """

    @abc.abstractmethod
    def add_message(self, message) -> None:
        pass

    @abc.abstractmethod
    def generate_response(self) -> str:
        pass

    @abc.abstractmethod
    def get_last_message(self) -> str:
        pass
