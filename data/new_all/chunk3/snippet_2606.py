# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69480350/typeerror-selector-object-is-not-iterable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from scrapy import Spider
    _l_(565376)

except ImportError:
    pass


class WikiSpider(_n_(565377, "Spider", lambda: Spider)):
    _l_(565396)

    name = 'wiki'
    _l_(565378)
    allowed_domains = ['wikipedia.com']
    _l_(565379)
    start_urls = ['https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States']
    _l_(565380)

    def parse(self, response):
        _l_(565395)

        Tabel=_c_(565383, _a_(565382, _n_(565381, "response", lambda: response), "xpath"), '//table[contains(@class,"wikitable sortable")]')[0]
        _l_(565384)
        for tabel in _n_(565385, "Tabel", lambda: Tabel):
            _l_(565394)

            state=_c_(565390, _a_(565389, _c_(565388, _a_(565387, _n_(565386, "tabel", lambda: tabel), "xpath"), './/tbody/tr/th/a/text()')[1:], "extract"))
            _l_(565391)
            yield{
                  _n_(565392, "state", lambda: state)
              }
            _l_(565393)