# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73861078/scrapy-attributeerror-module-openssl-ssl
# QuoteSpider.py

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import scrapy
    _l_(448771)

except ImportError:
    pass


class QuoteSpider(_a_(448773, _n_(448772, "scrapy", lambda: scrapy), "Spider")):
    _l_(448785)

    name = 'quotes'
    _l_(448774)
    start_urls = [
        'http://quotes.toscrape.com/'
    ]
    _l_(448775)

    def parse(self, response):
        _l_(448784)

        title = _c_(448780, _a_(448779, _c_(448778, _a_(448777, _n_(448776, "response", lambda: response), "css"), 'title'), "get"))
        _l_(448781)
        yield {'titletext': _n_(448782, "title", lambda: title)}
        _l_(448783)