from modules.vocabulary.abstract_message import AbstractMessage
from xml.etree.ElementTree import Element
from modules.condition import ConditionsJson


class OnMessage(AbstractMessage):
    def __init__(self, element: Element, conditions: ConditionsJson) -> None:
        from modules.vocabulary import Message, RandomMessage
        base_attributes = dict(where="public", condition=ConditionsJson.NOT_BY_BOT)
        super().__init__(element, conditions, base_attributes)
        self.messages = list()
        for child in element.findall("./"):
            if child.tag == "message":
                self.messages.append(Message(child, conditions, base_attributes))
            elif child.tag == "random_message":
                self.messages.append(RandomMessage(child, conditions, base_attributes))
            else:
                assert False, "The children of \"<on_message>\" need be \"<message>\" or \"<random_message>\"."
