from modules.vocabulary.abstract_message import AbstractMessage
from xml.etree.ElementTree import Element
from modules.condition import Condition, ConditionsJson


class Reply(AbstractMessage):
    def __init__(self, element: Element, where: str, condition: Condition, conditions: ConditionsJson) -> None:
        super().__init__(element, where, condition, conditions)
        self.reply = element.text
