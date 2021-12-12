# Define your item pipelines here
#
# Don't forget to add your queue to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter
import logging

from common import shared_queue
from scraper.items import ProductScrapingResult


class ScraperPipeline:
    def process_item(self, item: ProductScrapingResult, spider):
        logging.info('Process item %s', item)
        shared_queue.get_flow_queue().process_product(item)
