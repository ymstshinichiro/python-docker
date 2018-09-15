import json
import xmltodict

def main():
    json_text = file_read('../json/data.json')
    json_data = json.loads(json_text)

    xml_text = file_read('../xml/data.xml')
    xml_data = xmltodict.parse(xml_text)

    print('-- json_data --------------')
    print(json_data)
    print('-- xml_data --------------')
    print(xml_data)

    print('\n-- json_data["employees"] --------------')
    for emp in json_data['employees']:
        print(emp['name'])

    print('-- xml_data["root"]["employees"] --------------')
    for emp in xml_data['root']['employees']:
        print(emp['name'])


def file_read(path):
    with open(path, 'r') as file:
        text = file.read()
    return text

main()
