# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68474331/scrapy-nameerror-with-item-pipeline-when-calling-from-different-file
#testing.py
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import scraper_control
    _l_(641733)

except ImportError:
    pass
try:
    import json
    _l_(641735)

except ImportError:
    pass

def runScraper(spider):
    _l_(641752)

    sc= _n_(641736, "scraper_control", lambda: scraper_control)
    _l_(641737)
    scraper_results = _c_(641741, _a_(641739, _n_(641738, "sc", lambda: sc), "runspider"), _n_(641740, "spider", lambda: spider))
    _l_(641742)
    json_result = _c_(641746, _a_(641744, _n_(641743, "json", lambda: json), "dumps"), _n_(641745, "scraper_results", lambda: scraper_results))
    _l_(641747)
    _c_(641750, _n_(641748, "print", lambda: print), _n_(641749, "json_result", lambda: json_result))
    _l_(641751)

_c_(641754, _n_(641753, "runScraper", lambda: runScraper), "test_quotes")
_l_(641755)