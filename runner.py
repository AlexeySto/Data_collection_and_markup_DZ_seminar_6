from scrapy.crawler import CrawlerProcess 
from scrapy.utils.reactor import install_reactor 
from scrapy.utils.log import configure_logging 
from scrapy.utils.project import get_project_settings 
from unsplash_scraper.spiders.unsplash_spider import UnsplashSpider


def run_spider():
    configure_logging()
    install_reactor("twisted.internet.asyncioreactor.AsyncioSelectorReactor")
    proccess = CrawlerProcess(get_project_settings())
    proccess.crawl(UnsplashSpider)
    proccess.start()

if __name__ == '__main__':
    run_spider()
