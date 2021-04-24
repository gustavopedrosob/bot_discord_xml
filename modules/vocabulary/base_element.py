from xml.etree.ElementTree import Element


class BaseElement:
    def __init__(self, element: Element, attrs: list[str]) -> None:
        for attr in element.attrib.keys():
            if attr not in attrs:
                raise ValueError(f"Argument \"{attr}\" not exists!")
