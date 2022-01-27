import os

from scrapy.cmdline import execute

os.environ.setdefault('SCRAPY_SETTINGS_MODULE', 'scraper.settings')

if __name__ == '__main__':
    execute()
