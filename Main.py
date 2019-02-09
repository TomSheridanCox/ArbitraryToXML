import xml.etree.cElementTree as ET
import xml.dom.minidom as MD
import json
from sys import argv


def prettyPrintXML(root):
    tree = ET.tostring(root)
    print(MD.parseString(tree).toprettyxml())


def writeXML(root, filename='output.xml'):
    tree = ET.ElementTree(root)
    tree.write(filename)


def readJSON(filename='input.json'):
    with open(filename) as f:
        return json.load(f)


def jsonToXML(data, root):
    for key,val in data.items():
        if isinstance(val, dict):
            branch = ET.SubElement(root, key)
            jsonToXML(val, branch)
        elif isinstance(val, list):
            branch = ET.SubElement(root, key, type="array")
            for item in val:
                ET.SubElement(branch, "value").text = str(item)
        else:
            ET.SubElement(root, key).text = str(val)
    return root


def main():
    root = ET.Element('root')
    converted = jsonToXML(readJSON(), root)
    prettyPrintXML(converted)
    writeXML(converted)


if __name__ == '__main__':
    main()
