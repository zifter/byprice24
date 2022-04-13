from common.shared_queue import CrawlerTarget
from crawler.agent import get_agent
from django_rq import job
from scraper.items import ProductScrapingResult


@job
def scrape_target(target: CrawlerTarget):
    agent = get_agent()
    agent.scrape(target)


@job
def process_product(item: ProductScrapingResult):
    agent = get_agent()
    agent.process_scraping_result(item)
