from modules.vocabulary.abstract_message import AbstractMessage
from xml.etree.ElementTree import Element
from modules.condition import Condition, ConditionsJson


class AbstractMultipleMessage(AbstractMessage):
    def __init__(self, element: Element, conditions: ConditionsJson, inherited_arguments: dict):
        from modules.vocabulary import Reply
        super().__init__(element, conditions, inherited_arguments)
        answers = list(element.findall("./"))
        self.answers = [Reply(element, conditions, inherited_arguments) for element in answers
                        if element.tag.lower() == self.ANSWER]
