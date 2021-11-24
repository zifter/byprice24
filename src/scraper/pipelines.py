# Define your item pipelines here
#
# Don't forget to add your queue to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter
import logging

from common.shared_queue import get_flow_queue
from scraper.items import ProductItem


class ScraperPipeline:
    def process_item(self, item: ProductItem, spider):
        logging.info('Process item %s', item)
        get_flow_queue().process_product(item)
