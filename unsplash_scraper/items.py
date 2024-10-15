# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst


class UnsplashImageItem(scrapy.Item):
    image_url = scrapy.Field()
    title = scrapy.Field()
   