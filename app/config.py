import json
import sys
import os
from fileIO import IOmethods

class ConfigMethods():

    def input_path(self, message, config_param):
        filename = input(message)
        path = self.load_config(config_param) + filename
        if os.path.isfile(path):
            return path
        else:
            print('file note exist. Quit application.')
            sys.exit()
    
    def load_config(self, param_name):
        fIO = IOmethods()
        config_data = json.loads(fIO.ret_text("../config/Config.json"))
        return config_data[param_name]
