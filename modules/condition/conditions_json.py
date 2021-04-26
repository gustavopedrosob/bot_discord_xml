from modules.condition.condition import Condition


class ConditionsJson:
    NOT_BY_BOT = Condition("#not by bot", type="not by bot")
    FILE = "source/conditions.json"

    def __init__(self) -> None:
        from json import load
        from modules.condition import Conditions
        self.content, self.conditions, self.used_id = dict(), dict(), list()
        with open(self.FILE) as file:
            self.content = load(file)
        self.conditions.clear()
        self.used_id.clear()
        for key, value in self.content.items():
            if isinstance(value, dict):
                self.conditions[key] = Condition(key, **value)
            elif isinstance(value, list):
                self.conditions[key] = Conditions(key, value, self)

    def load(self):
        self.__init__()

    def get_condition(self, name: str):
        from modules.condition import ConditionBase
        get_mode = ConditionBase.get_mode(name)
        condition = self.conditions.get(name)
        if get_mode == "id" and condition and name in self.used_id:
            raise SyntaxError(f"The id \"{name}\" cant be used more than 1 time!")
        elif condition:
            return condition
        elif not condition and get_mode == "id":
            raise NameError(f"Id \"{name}\" not exists!")
        elif not condition and get_mode == "class":
            raise ValueError(f"Class \"{name}\" not exists!")
        else:
            raise ValueError(f"Invalid name \"{name}\" it need has \".\" or \"#\" at start of the word.")
