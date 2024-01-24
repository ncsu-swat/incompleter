# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/48591663/python-3-6-typeerror-module-object-is-not-callable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import re
    _l_(390528)

except ImportError:
    pass
try:
    from crawler import Crawler, CrawlerCache
    _l_(390530)

except ImportError:
    pass

if _n_(390531, "__name__", lambda: __name__) == "__main__":
    _l_(390567)

    # Using SQLite as a cache to avoid pulling twice
    crawler = _c_(390535, _n_(390532, "Crawler", lambda: Crawler), _c_(390534, _n_(390533, "CrawlerCache", lambda: CrawlerCache), 'crawler.db'))
    _l_(390536)
    root_re = _a_(390540, _c_(390539, _a_(390538, _n_(390537, "re", lambda: re), "compile"), '^/$'), "match")
    _l_(390541)
    _c_(390545, _a_(390543, _n_(390542, "crawler", lambda: crawler), "crawl"), 'http://techcrunch.com/', no_cache=_n_(390544, "root_re", lambda: root_re))
    _l_(390546)
    _c_(390550, _a_(390548, _n_(390547, "crawler", lambda: crawler), "crawl"), 'http://www.engadget.com/', no_cache=_n_(390549, "root_re", lambda: root_re))
    _l_(390551)
    _c_(390555, _a_(390553, _n_(390552, "crawler", lambda: crawler), "crawl"), 'http://gizmodo.com/', no_cache=_n_(390554, "root_re", lambda: root_re))
    _l_(390556)
    _c_(390560, _a_(390558, _n_(390557, "crawler", lambda: crawler), "crawl"), 'http://www.zdnet.com/', no_cache=_n_(390559, "root_re", lambda: root_re))
    _l_(390561)
    _c_(390565, _a_(390563, _n_(390562, "crawler", lambda: crawler), "crawl"), 'http://www.wired.com/', no_cache=_n_(390564, "root_re", lambda: root_re))
    _l_(390566)