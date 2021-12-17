from common.shared_queue import ScrapingTarget
from crawler.agent import get_agent
from django_rq import job
from scraper.items import ProductScrapingResult
from search.models import QueryHistory


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
    QueryHistory.objects.create(query=query.lower(), number_found_products=number_found_products)
