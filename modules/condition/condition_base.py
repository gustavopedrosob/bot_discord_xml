class ConditionBase:
    def __init__(self, name: str):
        self.name = name
        self.class_or_id = ConditionBase.is_class_or_id(self.name)

    @staticmethod
    def is_class_or_id(name: str):
        if name.startswith("."):
            return "class"
        elif name.startswith("#"):
            return "id"
        else:
            raise SyntaxError("To create a condition object, you need put a special character at start of word like"
                              " \"#\" to create a modules or \".\" to a id.")
