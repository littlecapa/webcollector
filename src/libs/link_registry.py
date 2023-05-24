import pandas as pd
import datetime

import logging
logger = logging.getLogger()

import src.libs.file_lib as fl

FILENAME = "link_registry.csv"

COLUMN_NAMES = ['Url', 'Pattern', 'Frequency', 'LastCheck', 'Path']
COLUMN_TYPES = [('Url', 'object'), ('Frequency', 'int64'), ('Pattern', 'object'), ('LastCheck', 'datetime64[ns]'), ('Path', 'object')]

class LinkRegistry:

    def __init__(self, registry_path):
        self.registry_path = registry_path
        new = fl.create_path(self.registry_path)
        if new:
            self.init_registry()
        else:
            self.registry = pd.read_csv(fl.file_path(self.registry_path, FILENAME))
            logger.debug(f"Read Link Registry")
    
    def __del__(self):
        self.save()

    def save(self):
        if fl.path_exist(self.registry_path):
            self.registry.to_csv(fl.file_path(self.registry_path, FILENAME), index = False)
            logger.debug(f"Link Registry saved")

    def init_registry(self):
        self.registry = pd.DataFrame(columns=COLUMN_NAMES)
        self.registry = self.registry.astype(dict(COLUMN_TYPES))
        self.save()

    def add_url(self, url, pattern, frequency, path):
        new_url = {
                    'Url': url, 
                    'Pattern': pattern, 
                    'Frequency': frequency,
                    'LastCheck': datetime.datetime.now(),
                    'Path': path
                    }
        self.registry = pd.concat([self.registry, pd.DataFrame([new_url])], ignore_index = True)