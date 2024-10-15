import scrapy 
from scrapy.http import HtmlResponse
from scrapy.loader import ItemLoader
from ..items import UnsplashImageItem

class UnsplashSpider(scrapy.Spider):
    name = "unsplash_spider"
    allowed_domains = ["unsplash.com"]
    start_urls = ['https://unsplash.com']

    def parse(self, response: HtmlResponse):
        # Получаем ссылки на фотографии
        images = response.xpath('//a[@itemprop="contentUrl"]')
        for image in images:
           yield response.follow(image, self.parse_image)

    def parse_image(self, response):
        loader = ItemLoader(item=UnsplashImageItem(),response=response)
        loader.add_xpath('title', '//img[@itemprop="thumbnailUrl"]/@alt')
        loader.add_xpath('image_url', '//img[@itemprop="thumbnailUrl"]/@src')
        yield loader.load_item()
        