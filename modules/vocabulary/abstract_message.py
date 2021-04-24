from modules.vocabulary.base_element import BaseElement
from modules.condition import Condition, ConditionsJson
from xml.etree.ElementTree import Element
from discord import Message


class AbstractMessage(BaseElement):
    ANSWER = "ANSWER"
    BAN = "ban"
    KICK = "kick"
    CONSEQUENCES = [BAN, KICK]
    PUBLIC = "public"
    PRIVATE = "private"
    PLACES = [PUBLIC, PRIVATE]
    ID = "id"
    CLASS = "class"
    WHERE = "where"
    DELAY = "delay"
    EMOTES_BOT = "emotes_bot"
    EMOTES_AUTHOR = "emotes_author"
    CONSEQUENCE = "consequence"
    ATTRS = [ID, CLASS, WHERE, DELAY, EMOTES_BOT, EMOTES_AUTHOR, CONSEQUENCE]

    def __init__(self, element: Element, where: str, condition: Condition, conditions: ConditionsJson):
        from modules.assertion import assert_string_in_list, assert_to_entire_number
        super().__init__(element, self.ATTRS)
        self.condition = condition
        self.reply = ""
        consequence = element.attrib.get(self.CONSEQUENCE)
        self.consequence = assert_string_in_list(
            consequence, "The \"consequence\" attribute need to be \"ban\" or \"kick\".", self.CONSEQUENCES) \
            if consequence else ""
        emotes_bot = element.attrib.get(self.EMOTES_BOT)
        self.emotes_bot = self.get_emotes(emotes_bot) if emotes_bot else ""
        emotes_author = element.attrib.get(self.EMOTES_AUTHOR)
        self.emotes_author = self.get_emotes(emotes_author) if emotes_author else ""
        delay = element.attrib.get(self.DELAY, "")
        self.delay = assert_to_entire_number(delay, "The \"delay\" attribute need to be a entire number.") \
            if delay else 0
        where_attr = element.attrib.get(self.WHERE)
        self.where = assert_string_in_list(
            where_attr.lower(), "The \"where\" attribute need to be \"private\" or \"public\".", self.PLACES) \
            if where_attr else where
        _class = element.attrib.get(self.CLASS)
        _id = element.attrib.get(self.ID)
        if _class and _id:
            raise SyntaxError("You cant put a class and a id in a element message.")
        elif _class:
            self.condition = conditions.get_condition("." + _class)
        elif _id:
            self.condition = conditions.get_condition("#" + _id)

    def format_to_send(self, message: Message) -> str:
        from datetime import datetime
        return self.reply.format(
            now=datetime.now(),
            guild_name=message.guild.name,
            channel_name=message.channel.name,
            author_name=message.author.display_name)

    async def send(self, message: Message):
        from asyncio import sleep
        from discord import Member, User
        if self.condition(message):
            if isinstance(message.author, User) and not isinstance(message.author, Member) and self.consequence:
                pass
            elif self.consequence and isinstance(message.author, Member):
                await message.author.ban() if self.consequence == self.BAN else await message.author.kick()
            else:
                await sleep(self.delay) if self.delay else None
                for emote in self.emotes_author:
                    await message.add_reaction(emote)
                channel = await message.author.create_dm() if self.where == self.PRIVATE else message.channel
                message_sent = await channel.send(self.format_to_send(message))
                for emote in self.emotes_bot:
                    await message_sent.add_reaction(emote)

    @staticmethod
    def get_emotes(emotes: str) -> str:
        from emoji import emoji_lis
        emotes = emoji_lis(emotes)
        if len(emotes) > 24:
            raise SyntaxError("You cant put more than 24 emotes in a message.")
        return "".join([emoji["emoji"] for emoji in emotes])
