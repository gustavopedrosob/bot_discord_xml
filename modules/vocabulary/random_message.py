from modules.vocabulary.attributes_message import AttributesMessage
from modules.vocabulary.abstract_message import AbstractMessage
from modules.vocabulary.answer import Answer
from modules.vocabulary.attributes.int_attribute import IntAttribute
from discord import Message
from xml.etree.ElementTree import Element


class RandomMessage(AbstractMessage, AttributesMessage):
    def __init__(self, element: Element):
        RandomMessage.ATTRS.append(IntAttribute("get", default=1))
        super().__init__(element)

    async def send(self, message: Message):
        from random import randint
        answers = [child for child in self.children if isinstance(child, Answer)]
        selecteds = []
        repeat = self.get
        while repeat:
            index = randint(0, len(answers) - 1)
            answer = answers[index]
            selecteds.append(answer)
            answers.remove(answer)
            repeat -= 1
        for selected_answer in selecteds:
            await selected_answer.send(message)
