# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from scrapy.pipelines.images import ImagesPipeline
import csv
import scrapy
import hashlib


class UnsplashScraperPipeline:
    def open_spider(self, spider):
        # Настройки для сохранения в CSV
        self.csv_file = open(f"{spider.name}.csv", "w", newline="", encoding="utf-8")
        self.csv_writer = csv.writer(self.csv_file)
        self.csv_writer.writerow(['title', 'image_url'])

    def close_spider(self, spider):
        # Закрытие CSV файла
        self.csv_file.close()
    
    def process_item(self, item, spider):
        # Сохранение данных в CSV
        for k in range(len(item['image_url'])):
            try:
                self.csv_writer.writerow([item['title'][k], item['image_url'][k]])
            except Exception as e:
                print(e)   
        return item
 
class UnsplashImagesPipeline(ImagesPipeline):
    count = 1
    def get_media_requests(self, item, info):
        for item_url in item['image_url']:
            if item['image_url']:
                try:
                    print(self.count)
                    print(item['image_url'])
                    self.count += 1
                    yield scrapy.Request(item_url)
                except Exception as e:
                    print(e)
                    