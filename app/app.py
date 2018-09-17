import sys
import json
import xmltodict
from config import ConfigMethods
from fileIO import IOmethods

global conf
conf = ConfigMethods()

def main():
    fIO = IOmethods()
    
    mode = input('Please select extension of data file (json or xml).\n input j or x :')
    MESSAGE = 'Please enter the fileName to load'
    if mode == 'j':    
        json_data = json.loads(fIO.ret_text(conf.input_path(MESSAGE + '(json) :', 'JsonDir')))
        records = json_data["employees"]
    elif mode == 'x':
        xml_data = xmltodict.parse(fIO.ret_text(conf.input_path(MESSAGE + '(xml) :', 'XmlDir')))
        records = xml_data["root"]["employees"]
    else:
        print('Input was an exception, so the application terminates.')
        sys.exit()

    for r in records:
        concat_str_orderby_list(r)


# config の DataLabelList から読み取った配列の順番で文字列を連結する
def concat_str_orderby_list(list_objects):
    ret_string = ""

    labels = conf.load_config('DataLabelList')
    for label in labels:
        ret_string = ret_string + list_objects[label] + "," 

    ret_string = ret_string[:-1] + "\n"
    print(ret_string)
    return ret_string

main()
