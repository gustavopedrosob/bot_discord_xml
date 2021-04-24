from modules.vocabulary.abstract_message import AbstractMessage
from xml.etree.ElementTree import Element
from modules.condition import ConditionsJson


class OnMessage(AbstractMessage):
    def __init__(self, element: Element, conditions: ConditionsJson) -> None:
        from modules.vocabulary import Message
        super().__init__(element, "public", ConditionsJson.NOT_BY_BOT, conditions)
        self.messages = [Message(e, self.where, self.condition, conditions) for e in element.iter("message")]
