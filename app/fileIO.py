
class IOmethods():

    def ret_text(self, path):
        with open(path, 'r') as file:
            text = file.read()
        return text
