import scrapy

class CountryDataSpider(scrapy.Spider):
    name = "country_data_spider"
    start_urls = ['https://en.wikipedia.org/wiki/Template:Visa_requirements']
    
    def parse(self, response):
        for country in response.css('div/ul/li'):
            yield {
                'text': country.css('a::text').extract_first(),
            }