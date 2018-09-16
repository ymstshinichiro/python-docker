import json
import xmltodict
from config import ConfigMethods

global config_obj
config_obj = ConfigMethods()

def main():
    mode = input('Please select extension of data file (json or xml).\n input j or x :')

    if mode == 'j':    
        path = config_obj.valid_filepath('Please enter the fileName to load (json) :', 'JsonDir')
        json_data = json.loads(config_obj.file_read(path))
        records = json_data["employees"]
    elif mode == 'x':
        path = config_obj.valid_filepath('Please enter the fileName to load (xml) :', 'XmlDir')
        xml_data = xmltodict.parse(config_obj.file_read(path))
        records = xml_data["root"]["employees"]

    for r in records:
        concat_str_orderby_list(r)


# config の DataLabelList から読み取った配列の順番で文字列を連結する
def concat_str_orderby_list(list_objects):
    ret_string = ""

    labels = config_obj.load_config('DataLabelList')
    for label in labels:
        ret_string = ret_string + list_objects[label] + "," 

    ret_string = ret_string[:-1] + "\n"
    print(ret_string)
    return ret_string

main()
