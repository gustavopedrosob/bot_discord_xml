from xml.etree.ElementTree import Element


class BaseElement:
    ATTRS = []

    def __init__(self, element: Element) -> None:
        for attr in element.attrib.keys():
            if attr not in self.ATTRS:
                raise ValueError(f"Argument \"{attr}\" not exists!")
