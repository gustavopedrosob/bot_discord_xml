from bot import Bot
from json import load

with open("source/config.json", "r") as config_file:
    config = load(config_file)

bot = Bot()
bot.run(config["token"])
