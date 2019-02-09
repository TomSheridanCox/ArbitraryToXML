import xml.etree.cElementTree as et
import xml.dom.minidom as md
import json


def pretty_print_xml(root):
    tree = et.tostring(root)
    print(md.parseString(tree).toprettyxml())


def write_xml(root, filename='output.xml'):
    tree = et.ElementTree(root)
    tree.write(filename)


def read_json(filename='input.json'):
    with open(filename) as f:
        return json.load(f)


def json_to_xml(data, root):
    for key,val in data.items():
        if isinstance(val, dict):
            branch = et.SubElement(root, key)
            json_to_xml(val, branch)
        elif isinstance(val, list):
            branch = et.SubElement(root, key, type="array")
            for item in val:
                et.SubElement(branch, "value").text = str(item)
        else:
            et.SubElement(root, key).text = str(val)
    return root


def main():
    root = et.Element('root')
    converted = json_to_xml(read_json(), root)
    pretty_print_xml(converted)
    write_xml(converted)


if __name__ == '__main__':
    main()
