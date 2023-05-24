import os
import shutil

import logging
logger = logging.getLogger()

import src.libs.file_lib as fl

from src.libs.link_registry import LinkRegistry as lr

META_DIR = "meta"
DOWNLOAD_DIR = "download"

DEL_SECRET = "xxx"

class Collector:

    def __init__(self, destination_path ):
        self.destination_path = destination_path
        _ = fl.create_path(self.destination_path)
        self.init_collector_resources()
            
    def __str__(self):
        return f"{self.destination_path})"
    
    def del_all(self, secret):
        fl.del_all(self.destination_path, secret, DEL_SECRET)

    def add_url(self, url, pattern, frequency, path):
        self.lreg.add_url(url, pattern, frequency, path)

    def init_collector_resources(self):
        self.download_path = os.path.join(self.destination_path, DOWNLOAD_DIR)
        _ = fl.create_path(self.download_path)
        self.meta_path = os.path.join(self.destination_path, META_DIR)
        self.lreg = lr(self.meta_path)
        
