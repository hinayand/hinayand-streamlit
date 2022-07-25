import json


class ConfigTools(object):
    def __init__(self, path):
        self.path = path
        self.config = {}

    def add_config(self, key, value):
        self.config[key] = value

    def del_config(self, key):
        del self.config[key]

    def edit_config(self, key, value):
        self.config[key] = value

    def get_config(self, key):
        return self.config[key]

    def get_configs(self):
        return self.config

    def get_length(self):
        return len(self.config)

    def key_is_exist(self, key):
        return key in self.config

    def value_is_exist(self, value):
        for key in self.config:
            if self.config[key] == value:
                return True
        return False

    def sort_config(self):
        return sorted(self.config.items(), key=lambda x: x[0])

    def save_config(self):
        with open(self.path, 'w', encoding='utf-8') as f:
            json.dump(self.config, f)

    def load_config(self):
        with open(self.path, 'r', encoding='utf-8') as f:
            self.config = json.load(f)
