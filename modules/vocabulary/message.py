from modules.vocabulary.attributes_message import AttributesMessage
from discord import Message as DMessage
from modules.vocabulary.abstract_message import AbstractMessage
from xml.etree.ElementTree import Element
from modules.vocabulary.answer import Answer


class Message(AbstractMessage):
    CHILDREN = AttributesMessage.CHILDREN
    ATTRS = AttributesMessage.ATTRS

    def __init__(self, element: Element):
        super().__init__(element)

    async def send(self, message: DMessage) -> None:
        answers = [child for child in self.children if isinstance(child, Answer)]
        if answers:
            for answer in answers:
                await answer.send(message)
        else:
            await super().send(message)
