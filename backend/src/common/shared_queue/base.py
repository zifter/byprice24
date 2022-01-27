import abc

from .structs import ScrapingTarget


class FlowQueueBase:
    @abc.abstractmethod
    def scrape(self, target: ScrapingTarget):
        pass

    @abc.abstractmethod
    def process_product(self, product):
        pass

    @abc.abstractmethod
    def push_query(self, query, number_found_products):
        pass
