import scrapy


class BrickSetSpider(scrapy.Spider):
    name = "brickset_spider"
    start_urls = ['https://en.wikipedia.org/wiki/Category:Visa_requirements_by_nationality']