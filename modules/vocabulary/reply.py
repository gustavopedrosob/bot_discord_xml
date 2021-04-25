from modules.vocabulary.abstract_message import AbstractMessage
from xml.etree.ElementTree import Element
from modules.condition import ConditionsJson


class Reply(AbstractMessage):
    def __init__(self, element: Element, conditions: ConditionsJson, inherited_arguments: dict) -> None:
        super().__init__(element, conditions, inherited_arguments)
        self.reply = element.text
