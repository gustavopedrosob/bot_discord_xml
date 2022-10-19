from modules.vocabulary.message import Message
from modules.vocabulary.attributes_message import AttributesMessage
from xml.etree.ElementTree import Element
from modules.vocabulary.node import Node


class OnMessage(Node):
    CHILDREN = {"message": Message}
    ATTRS = AttributesMessage.ATTRS

    def __init__(self, element: Element, **kwargs):
        super().__init__(element, **kwargs)
