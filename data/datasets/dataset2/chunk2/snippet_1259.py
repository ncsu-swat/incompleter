#Source: https://stackoverflow.com/questions/73861078/scrapy-attributeerror-module-openssl-ssl
# QuoteSpider.py

import scrapy


class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    def parse(self, response):
        title = response.css('title').get()
        yield {'titletext': title}