import xml.etree.cElementTree as et
import xml.dom.minidom as md
import json
import argparse

def pretty_print_xml(root):
    tree = et.tostring(root)
    print(md.parseString(tree).toprettyxml())


def write_xml(root, filename):
    tree = et.ElementTree(root)
    tree.write(filename)


def read_json(filename):
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
    parser = argparse.ArgumentParser(description='Convert arbitrary unformatted or formatted text to arbitrary XML')
    parser.add_argument('-i','--inputFile', dest='inputFile', help='File from which to read input text - defaults to input.json')
    parser.add_argument('-o','--outputFile', dest='outputFile', help='File to output converted text to - defaults to output.xml')
    args = parser.parse_args()
    root = et.Element('root')
    converted = json_to_xml(read_json(filename='input.json' if args.inputFile == None else args.inputFile), root)
    pretty_print_xml(converted)
    write_xml(converted, filename='output.xml' if args.inputFile == None else args.inputFile)


if __name__ == '__main__':
    main()
