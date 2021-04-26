class ConditionBase:
    def __init__(self, name: str or None = None):
        self.name = name

    
    @staticmethod
    def get_mode(name: str or None):
        if name is None:
            return "anonymous"
        if name.startswith("."):
            return "class"
        elif name.startswith("#"):
            return "id"
        else:
            raise SyntaxError("To create a condition object, you need put a special character at start of word like"
                              " \"#\" to create a modules or \".\" to a id.")
