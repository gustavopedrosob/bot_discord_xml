from modules.vocabulary.attributes import Attributes
from xml.etree.ElementTree import Element


class Node:
    CHILDREN = {}
    ATTRS: Attributes = None

    def __init__(self, element: Element):
        self.parent = None
        self.text = element.text
        self.children = []
        self.attributes = element.attrib
        if self.ATTRS:
            self.update_attributes()
            self.validate()
        self.set_attributes()
        self.find_children(element)

    def find_children(self, element: Element):
        children = element.findall("./")
        for child in children:
            self.add_child(self.CHILDREN[child.tag](child))
    
    def add_child(self, node):
        self.children.append(node)
        node.parent = self
        node.inherit()
    
    def remove_child(self, node):
        self.children.remove(node)
        node.parent = None

    def update_attributes(self):
        self.attributes.update(self.ATTRS.values(self.attributes))

    def inherit(self):
        if self.parent:
            self.attributes.update(self.parent.attributes)

    def execute(**kwargs):
        pass

    def validate(self):
        self.ATTRS.validate(self.attributes)

    def set_attributes(self):
        for key, value in self.attributes.items():
            setattr(self, key, value)