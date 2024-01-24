# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59993853/why-does-nameerror-name-not-defined-occur-when-executing-python-file-external
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(668299)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(668301)

except ImportError:
    pass
try:
    from multiprocessing import Pool
    _l_(668303)

except ImportError:
    pass
try:
    from datetime import timedelta, date
    _l_(668305)

except ImportError:
    pass
try:
    from external_functions import get_api_item
    _l_(668307)

except ImportError:
    pass

def date_range(start_date, end_date):
    _l_(668321)

    for n in _c_(668314, _n_(668308, "range", lambda: range), _c_(668313, _n_(668309, "int", lambda: int), _a_(668312, (_n_(668310, "end_date", lambda: end_date) - _n_(668311, "start_date", lambda: start_date)), "days"))):
        _l_(668320)

        yield _n_(668315, "start_date", lambda: start_date) + _c_(668318, _n_(668316, "timedelta", lambda: timedelta), _n_(668317, "n", lambda: n))
        _l_(668319)

start_date = _c_(668323, _n_(668322, "date", lambda: date), 2020, 1, 29)
_l_(668324)
end_date = _c_(668326, _n_(668325, "date", lambda: date), 2020, 1, 30)
_l_(668327)
date_list = []
_l_(668328)

for single_date in _c_(668332, _n_(668329, "date_range", lambda: date_range), _n_(668330, "start_date", lambda: start_date), _n_(668331, "end_date", lambda: end_date)):
    _l_(668340)

    _c_(668338, _a_(668334, _n_(668333, "date_list", lambda: date_list), "append"), _c_(668337, _a_(668336, _n_(668335, "single_date", lambda: single_date), "strftime"), '%Y-%m-%d'))
    _l_(668339)

if _n_(668341, "__name__", lambda: __name__) == '__main__':
    _l_(668360)

    global results
    _l_(668342)
    p = _c_(668344, _n_(668343, "Pool", lambda: Pool), 20)
    _l_(668345)
    results = _c_(668350, _a_(668347, _n_(668346, "p", lambda: p), "map"), _n_(668348, "get_api_item", lambda: get_api_item), _n_(668349, "date_list", lambda: date_list))
    _l_(668351)
    _c_(668354, _a_(668353, _n_(668352, "p", lambda: p), "terminate"))
    _l_(668355)
    _c_(668358, _a_(668357, _n_(668356, "p", lambda: p), "join"))
    _l_(668359)

result = _c_(668364, _a_(668362, _n_(668361, "pd", lambda: pd), "concat"), _n_(668363, "results", lambda: results))
_l_(668365)