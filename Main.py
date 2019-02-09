import xml.etree.cElementTree as ET
import xml.dom.minidom as MD
import json


def pretty_print_xml(root):
    tree = ET.tostring(root)
    print(MD.parseString(tree).toprettyxml())


def write_xml(root, filename='output.xml'):
    tree = ET.ElementTree(root)
    tree.write(filename)


def read_json(filename='input.json'):
    with open(filename) as f:
        return json.load(f)


def json_to_xml(data, root):
    for key,val in data.items():
        if isinstance(val, dict):
            branch = ET.SubElement(root, key)
            json_to_xml(val, branch)
        elif isinstance(val, list):
            branch = ET.SubElement(root, key, type="array")
            for item in val:
                ET.SubElement(branch, "value").text = str(item)
        else:
            ET.SubElement(root, key).text = str(val)
    return root


def main():
    root = ET.Element('root')
    converted = json_to_xml(read_json(), root)
    pretty_print_xml(converted)
    write_xml(converted)


if __name__ == '__main__':
    main()
