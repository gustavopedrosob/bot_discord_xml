from modules.vocabulary.abstract_message import AbstractMessage
from xml.etree.ElementTree import Element
from modules.condition import Condition, ConditionsJson
from discord import Message as DMessage


class Message(AbstractMessage):
    def __init__(self, element: Element, where: str, condition: Condition, conditions: ConditionsJson) -> None:
        from modules.vocabulary import Reply
        super().__init__(element, where, condition, conditions)
        answers = list(element.iter(self.ANSWER))
        self.multiple = len(answers) > 0
        if self.multiple:
            self.answers = [Reply(r, self.where, condition, conditions) for r in answers]
        else:
            self.reply = element.text

    async def send(self, message: DMessage) -> None:
        if self.multiple:
            for reply in self.answers:
                await reply.send(message)
        else:
            await super().send(message)
