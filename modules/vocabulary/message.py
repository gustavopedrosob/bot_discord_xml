from xml.etree.ElementTree import Element
from modules.condition import Condition, ConditionsJson
from discord import Message as DMessage
from modules.vocabulary.abstract_multiple_message import AbstractMultipleMessage


class Message(AbstractMultipleMessage):
    def __init__(self, element: Element, conditions: ConditionsJson, inherited_arguments: dict) -> None:
        super().__init__(element, conditions, inherited_arguments)

    async def send(self, message: DMessage) -> None:
        if self.answers:
            for reply in self.answers:
                await reply.send(message)
        else:
            await super().send(message)
