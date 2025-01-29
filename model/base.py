import xml.etree.ElementTree as ET

class Base:
    def __init__(self, file):
        self.tree = ET.parse(file)
        self.root = self.tree.getroot()

    def remove_namespaces(self, xml):
        for elem in xml.iter():
            if '}' in elem.tag:
                elem.tag = elem.tag.split('}', 1)[1]

    def read_tags(self, root_tag, register):
        self.remove_namespaces(self.root)
        if isinstance(register, tuple):
            for tag in register:
                value = next((data.text.strip() for data in self.root.find(root_tag) if data.tag == tag), None)
                if value:
                    return value
            return None
        return [data.text.strip() for data in self.root.find(root_tag) if data.tag == register][0]
