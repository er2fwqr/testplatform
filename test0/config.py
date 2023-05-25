import configparser
class IniConfig:
    def __init__(self):
        self.config=configparser.ConfigParser()
    def load_config(self,file_path):
        self.config.read(file_path)
    def get_value(self,section,option):
        return  self.config.get(section,option)
    def change_value(self,section,option):
        self.config.set(section=section,option=option)