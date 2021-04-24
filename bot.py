from discord import Client, Member, User, Intents, Message


class Bot(Client):
    def __init__(self):
        from modules.vocabulary.vocabulary import Vocabulary
        super().__init__(intents=Intents.all())
        self.vocabulary = Vocabulary()

    @staticmethod
    async def on_ready():
        print("Bot started")

    async def on_member_join(self, member: Member):
        pass

    async def on_message(self, message: Message):
        for msg in self.vocabulary.on_message_event.messages:
            await msg.send(message)
