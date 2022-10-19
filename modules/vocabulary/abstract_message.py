from modules.vocabulary.vocabulary import Vocabulary
from modules.vocabulary.node import Node
from discord import Message
from modules.condition.condition_base import RESPECTIVE_SYMBOLS
from xml.etree.ElementTree import Element

class AbstractMessage(Node):
    def __init__(self, element: Element):
        super().__init__(element)
        self.condition = self.get_condition()

    def format_to_send(self, message: Message) -> str:
        from datetime import datetime
        return self.reply.format(
            now=datetime.now(),
            guild_name=message.guild.name,
            channel_name=message.channel.name,
            author_name=message.author.display_name)

    def get_condition(self):
        for type in ["class", "id"]:
            if type in self.attributes:
                Vocabulary.CONDITIONS.get_condition(RESPECTIVE_SYMBOLS[type], self.attributes[type])

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
                text = self.format_to_send(message)
                if self.where == self.PRIVATE or self.where == self.BOTH_PLACES:
                    channel = await message.author.create_dm()
                    message_sent = await channel.send(text)
                    for emote in self.emotes_bot:
                        await message_sent.add_reaction(emote)
                if self.where == self.PUBLIC or self.where == self.BOTH_PLACES:
                    message_sent = await message.channel.send(text)
                    for emote in self.emotes_bot:
                        await message_sent.add_reaction(emote)