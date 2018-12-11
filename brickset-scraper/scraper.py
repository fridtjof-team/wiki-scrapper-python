import scrapy


class BrickSetSpider(scrapy.Spider):
    name = "brickset_spider"
    start_urls = ['https://en.wikipedia.org/w/api.php?action=parse&prop=text&page=Category:Visa_requirements_by_nationality&format=php']