from modules.vocabulary.abstract_message import AbstractMessage
from xml.etree.ElementTree import Element


class Answer(AbstractMessage):
    def __init__(element: Element):
        super().__init__(element)