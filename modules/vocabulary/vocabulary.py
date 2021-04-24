class Vocabulary:
    FILE = "source/vocabulary.xml"

    def __init__(self) -> None:
        from xml.etree.ElementTree import parse
        from modules.condition import ConditionsJson
        from modules.vocabulary import OnMessage
        tree = parse(self.FILE)
        self.conditions = ConditionsJson()
        self.on_message_event = OnMessage(tree.find("on_message"), self.conditions)

    def load(self):
        self.__init__()
