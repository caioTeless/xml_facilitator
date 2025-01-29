import xml.etree.ElementTree as ET

class Base:
    def __init__(self, file):
        self.tree = file
        self.root = self.tree.getroot()

    def remove_namespaces(xml):
        for elem in xml.iter():
            if '}' in elem.tag:
                elem.tag = elem.tag.split('}', 1)[1]




#ET.parse('file')