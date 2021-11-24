from scraper.items import ProductItem
from scraper.pipelines import ScraperPipeline


def test_scraper_pipeline_process_ok():
    pipeline = ScraperPipeline()
    item = ProductItem()
    assert pipeline.process_item(item, None) is None
