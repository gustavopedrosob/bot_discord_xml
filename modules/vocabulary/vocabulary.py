from modules.vocabulary.on_message import OnMessage
from xml.etree.ElementTree import parse
from modules.vocabulary.node import Node
from modules.condition.conditions_json import ConditionsJson

class Vocabulary(Node):
    CHILDREN = {"on_message": OnMessage}
    FILE = "source/vocabulary.xml"
    CONDITIONS = ConditionsJson()

    def __init__(self):
        tree = parse(self.FILE)
        element = tree.getroot()
        super().__init__(element)