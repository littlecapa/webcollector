import logging.config
import sys
sys.path.append('..')
from src.collector import Collector as col

folder = "/Users/littlecapa/data_lake/test_create"

def main():
    collector = col(folder)
    collector.del_all("xxx")

if __name__ == '__main__':
    logging.config.fileConfig('logging.ini')
    main()