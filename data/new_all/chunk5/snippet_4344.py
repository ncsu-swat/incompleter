# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59444515/attributeerror-nonetype-object-has-no-attribute-html
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from facebook_scraper import get_posts
    _l_(700785)

except ImportError:
    pass
try:
    import csv
    _l_(700787)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(700789)

except ImportError:
    pass
try:
    import sys
    _l_(700791)

except ImportError:
    pass
non_bmp_map = _c_(700798, _a_(700793, _n_(700792, "dict", lambda: dict), "fromkeys"), _c_(700797, _n_(700794, "range", lambda: range), 0x10000, _a_(700796, _n_(700795, "sys", lambda: sys), "maxunicode") + 1), 0xfffd)
_l_(700799)
csvFile = _c_(700801, _n_(700800, "open", lambda: open), 'nintendo.csv', 'a')
_l_(700802)
csvWriter = _c_(700806, _a_(700804, _n_(700803, "csv", lambda: csv), "writer"), _n_(700805, "csvFile", lambda: csvFile))
_l_(700807)
for post in _c_(700809, _n_(700808, "get_posts", lambda: get_posts), 'nintendo', pages=100):
    _l_(700824)

    _c_(700815, _n_(700810, "print", lambda: print), _c_(700814, _a_(700812, _n_(700811, "post", lambda: post)['text'], "translate"), _n_(700813, "non_bmp_map", lambda: non_bmp_map)))
    _l_(700816)
    _c_(700822, _a_(700818, _n_(700817, "csvWriter", lambda: csvWriter), "writerow"), [_c_(700821, _a_(700820, _n_(700819, "post", lambda: post)['text'], "encode"), 'utf-8')])
    _l_(700823)