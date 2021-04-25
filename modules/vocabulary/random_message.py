from modules.vocabulary.abstract_multiple_message import AbstractMultipleMessage
from xml.etree.ElementTree import Element
from modules.condition import ConditionsJson
from discord import Message


class RandomMessage(AbstractMultipleMessage):
    GET = "get"
    ATTRS = ["id", "class", "where", "delay", "emotes_bot", "emotes_author", "consequence", "get"]

    def __init__(self, element: Element, conditions: ConditionsJson, inherited_arguments: dict):
        super().__init__(element,  conditions, inherited_arguments)
        get = element.attrib.get(self.GET)
        if get:
            assert get.isdigit(), "The \"get\" attribute need to be a entire number."
            assert int(get) <= len(self.answers), "The \"get\" attribute cant be higher than the number of answers."
            self.get = int(get)
        else:
            self.get = 1
        self.__used_answers = list()

    async def send(self, message: Message):
        from random import randint
        if self.answers and self.condition(message):
            for x in range(0, self.get):
                answers = set(self.answers).difference(self.__used_answers)
                index = randint(0, len(answers) - 1)
                answer = list(answers)[index]
                await answer.send(message)
                self.__used_answers.append(answer)
            self.__used_answers.clear()
        else:
            await super().send(message)
