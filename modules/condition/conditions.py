from modules.condition.conditions_json import ConditionsJson
from modules.condition.condition_base import ConditionBase


class Conditions(ConditionBase):
    def __init__(self, name: str, conditions: list[dict, str], conditions_json: ConditionsJson) -> None:
        from modules.condition import Condition
        super().__init__(name)
        self.conditions = []
        for condition in conditions:
            if isinstance(condition, dict):
                self.conditions.append(Condition(**condition))
            elif isinstance(condition, str):
                if condition in conditions_json.conditions:
                    self.conditions.append(conditions_json.conditions[condition])
                # elif condition in condition.content.keys():
                #     raise error
                else:
                    raise NameError(f"Condition \"{condition}\" is not defined or referred before exists.")

    def __call__(self, arg):
        return all([condition(arg) for condition in self.conditions])

