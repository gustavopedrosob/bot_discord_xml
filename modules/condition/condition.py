from discord import Message
from operator import eq, contains
from modules.condition.condition_base import ConditionBase


class Condition(ConditionBase):
    CONDITIONS = {
        "true": lambda self, arg: True,
        "false": lambda self, arg: False,
        "by bot": lambda self, arg: arg.author.bot,
        "not by bot": lambda self, arg: not arg.author.bot,
        "message equal": lambda self, arg: self.__base_compare(arg.content, self.value, eq),
        "message not equal": lambda self, arg: not self.__base_compare(arg.content, self.value, eq),
        "name equal": lambda self, arg: self.__base_compare(arg.author.display_name, self.value, eq),
        "name not equal": lambda self, arg: not self.__base_compare(arg.author.display_name, self.value, eq),
        "guild name equal": lambda self, arg: self.__base_compare(arg.guild.name, self.value, eq),
        "guild name not equal": lambda self, arg: not self.__base_compare(arg.guild.name, self.value, eq),
        "channel name equal": lambda self, arg: self.__base_compare(arg.channel.name, self.value, eq),
        "channel name not equal": lambda self, arg: not self.__base_compare(arg.channel.name, self.value, eq),
        "message startswith": lambda self, arg: self.__base_compare(arg.content, self.value, str.startswith),
        "message not startswith": lambda self, arg: not self.__base_compare(arg.content, self.value, str.startswith),
        "name startswith": lambda self, arg: self.__base_compare(arg.author.display_name, self.value, str.startswith),
        "name not startswith": lambda self, arg: not self.__base_compare(
            arg.author.display_name, self.value, str.startswith),
        "guild name startswith": lambda self, arg: self.__base_compare(arg.guild.name, self.value, str.startswith),
        "guild name not startswith": lambda self, arg: not self.__base_compare(
            arg.guild.name, self.value, str.startswith),
        "message endswith": lambda self, arg: self.__base_compare(arg.content, self.value, str.endswith),
        "message not endswith": lambda self, arg: not self.__base_compare(arg.content, self.value, str.endswith),
        "name endswith": lambda self, arg: self.__base_compare(arg.author.display_name, self.value, str.endswith),
        "name not endswith": lambda self, arg: not self.__base_compare(
            arg.author.display_name, self.value, str.endswith),
        "guild name endswith": lambda self, arg: self.__base_compare(arg.guild.name, self.value, str.endswith),
        "guild name not endswith": lambda self, arg: not self.__base_compare(arg.guild.name, self.value, str.endswith),
        "value in message": lambda self, arg: self.__base_compare(self.value, arg.content, contains),
        "value not in message": lambda self, arg: not self.__base_compare(self.value, arg.content, contains),
        "value in name": lambda self, arg: self.__base_compare(self.value, arg.author.display_name, contains),
        "value not in name": lambda self, arg: not self.__base_compare(self.value, arg.author.display_name, contains),
        "value in guild name": lambda self, arg: self.__base_compare(self.value, arg.guild.name, contains),
        "value not in guild name": lambda self, arg: not self.__base_compare(self.value, arg.guild.name, contains)
    }
    TYPES = list(CONDITIONS.keys())
    FLAGS = ["lowercase"]
    ATTRS = ["type", "value", "flags"]

    def __init__(self, name: str, **kwargs) -> None:
        super().__init__(name)
        self.type = kwargs["type"]
        self.value = kwargs.get("value")
        self.flags = kwargs.get("flags")
        for attr in kwargs.keys():
            if attr not in self.ATTRS:
                raise SyntaxError(f"Invalid condition attribute \"{attr}\".")
        if self.type not in self.TYPES:
            raise ValueError(f"Type \"{self.type}\" not exists!")
        if isinstance(self.flags, list):
            for self.flag in self.flags:
                if self.flag not in self.FLAGS:
                    raise ValueError(f"Flag \"{self.flags}\" not exists")
        elif isinstance(self.flags, str):
            if self.flags not in self.FLAGS:
                raise ValueError(f"Flag \"{self.flags}\" not exists")
        elif self.flags is None:
            pass
        else:
            raise ValueError("Invalid type of flag, use string or list of string.")

    def __call__(self, arg: Message) -> bool:
        if isinstance(arg, Message):
            return self.CONDITIONS[self.type](self, arg)
        return False

    def __base_compare(self, value_1: str, value_2: str, func) -> bool:
        if self.flags is None:
            return func(value_1, value_2)
        else:
            if isinstance(self.flags, list):
                if "lowercase" in self.flags:
                    return func(value_1.lower(), value_2.lower())
            elif isinstance(self.flags, str):
                if "lowercase" == self.flags:
                    return func(value_1.lower(), value_2.lower())

