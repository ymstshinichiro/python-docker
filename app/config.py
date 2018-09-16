import json
import sys
import os

class ConfigMethods():

    def valid_filepath(self, message, config_param):
        filename = input(message)
        path = self.load_config(config_param) + filename
        if os.path.isfile(path):
            return path
        else:
            print('file note exist. Quit application.')
            sys.exit()

    def load_config(self, param_name):
        config_data = json.loads(self.file_read("../config/Config.json"))
        return config_data[param_name]

    def file_read(self, path):
        with open(path, 'r') as file:
            text = file.read()
        return text
