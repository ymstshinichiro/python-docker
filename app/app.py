import json
import xmltodict

def main():
    json_data = json.loads(file_read('../json/data.json'))
    xml_data = xmltodict.parse(file_read('../xml/data.xml'))

    print_with_header('-- json_data ---- ', json_data)
    print_with_header('-- xml_data ---- ', xml_data)

    print_foreach_with_header('-- json_data["employees"] -- ',  json_data['employees'], 'name')
    print_foreach_with_header('-- xml_data["root"]["employees"] -- ',  xml_data['root']['employees'], 'name')

def file_read(path):
    with open(path, 'r') as file:
        text = file.read()
    return text

def print_with_header(headertext, printobject):
    print(headertext)
    print(printobject)
    print()

def print_foreach_with_header(headertext, printobjects, printlabel):
    print(headertext)

    for obj in printobjects:
        print(obj[printlabel])

main()
