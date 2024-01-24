# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68474331/scrapy-nameerror-with-item-pipeline-when-calling-from-different-file
#scraper_control.py
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
spiders = {"test_quotes": _n_(582299, "ToScrapeCSSSpider", lambda: ToScrapeCSSSpider)}
_l_(582300)
items = []
_l_(582301)

class ItemCollectorPipeline(_n_(582302, "object", lambda: object)):
    _l_(582314)

    def __init__(self):
        _l_(582307)

        _n_(582303, "self", lambda: self).ids_seen = _c_(582305, _n_(582304, "set", lambda: set))
        _l_(582306)

    def process_item(self, item, spider):
        _l_(582313)

        _c_(582311, _a_(582309, _n_(582308, "items", lambda: items), "append"), _n_(582310, "item", lambda: item))
        _l_(582312)

crawler_process = _c_(582316, _n_(582315, "CrawlerProcess", lambda: CrawlerProcess), {
        "USER_AGENT": "scrapy",
        "LOG_LEVEL": "INFO",
        "ITEM_PIPELINES": {"__main__.ItemCollectorPipeline": 100},
    }
)
_l_(582317)

def runspider(spider):
    _l_(582330)

    _c_(582322, _a_(582319, _n_(582318, "crawler_process", lambda: crawler_process), "crawl"), _n_(582320, "spiders", lambda: spiders)[_n_(582321, "spider", lambda: spider)])
    _l_(582323)
    _c_(582326, _a_(582325, _n_(582324, "crawler_process", lambda: crawler_process), "start"))
    _l_(582327)
    aux = _n_(582328, "items", lambda: items)
    _l_(582329)
    return aux