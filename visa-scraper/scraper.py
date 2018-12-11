import scrapy

class CountryDataSpider(scrapy.Spider):
    name = "country_data_spider"
    start_urls = ['https://en.wikipedia.org/wiki/Template:Visa_requirements']
    
    def parse(self, response):
        SET_SELECTOR = '//*[contains(@class, \"navbox-list\")]/div/ul//li'
        for country in response.xpath(SET_SELECTOR):
            NAME_SELECTOR = 'a ::text'
            WIKI_LINK_SELECTOR = 'a ::attr(href)'
            yield {
                'name': country.css(NAME_SELECTOR).extract_first(),
                'wiki_link' : country.css(WIKI_LINK_SELECTOR).extract_first(),
            }