import logging.config

import sys
sys.path.append('..')
from src.collector import Collector as col

folder = "/Users/littlecapa/data_lake/test_create"

def main():
    collector = col(folder)
    collector.add_url("https://www.pegelonline.wsv.de/webservices/files/Wasserstand+Rohdaten/RHEIN/BINGEN", "down.csv", 2, "rhein/bingen")

if __name__ == '__main__':
    logging.config.fileConfig('logging.ini')
    main()