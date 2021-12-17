from common.shared_queue import ScrapingTarget
from crawler.agent import get_agent
from django_rq import job
from scraper.items import ProductScrapingResult


@job
def scrape_target(task: ScrapingTarget):
    agent = get_agent()
    agent.scrape(task)


@job
def process_product(item: ProductScrapingResult):
    agent = get_agent()
    agent.process_product(item)


@job
def push_query(query: str, number_found_products: int):
    agent = get_agent()
    agent.push_query(query, number_found_products)
