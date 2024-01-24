# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59993853/why-does-nameerror-name-not-defined-occur-when-executing-python-file-external
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(647770)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(647772)

except ImportError:
    pass
try:
    from multiprocessing import Pool
    _l_(647774)

except ImportError:
    pass
try:
    from datetime import timedelta, date
    _l_(647776)

except ImportError:
    pass
try:
    from external_functions import get_api_item
    _l_(647778)

except ImportError:
    pass

def date_range(start_date, end_date):
    _l_(647792)

    for n in _c_(647785, _n_(647779, "range", lambda: range), _c_(647784, _n_(647780, "int", lambda: int), _a_(647783, (_n_(647781, "end_date", lambda: end_date) - _n_(647782, "start_date", lambda: start_date)), "days"))):
        _l_(647791)

        yield _n_(647786, "start_date", lambda: start_date) + _c_(647789, _n_(647787, "timedelta", lambda: timedelta), _n_(647788, "n", lambda: n))
        _l_(647790)

start_date = _c_(647794, _n_(647793, "date", lambda: date), 2020, 1, 29)
_l_(647795)
end_date = _c_(647797, _n_(647796, "date", lambda: date), 2020, 1, 30)
_l_(647798)
date_list = []
_l_(647799)

for single_date in _c_(647803, _n_(647800, "date_range", lambda: date_range), _n_(647801, "start_date", lambda: start_date), _n_(647802, "end_date", lambda: end_date)):
    _l_(647811)

    _c_(647809, _a_(647805, _n_(647804, "date_list", lambda: date_list), "append"), _c_(647808, _a_(647807, _n_(647806, "single_date", lambda: single_date), "strftime"), '%Y-%m-%d'))
    _l_(647810)

if _n_(647812, "__name__", lambda: __name__) == '__main__':
    _l_(647831)

    global results
    _l_(647813)
    p = _c_(647815, _n_(647814, "Pool", lambda: Pool), 20)
    _l_(647816)
    results = _c_(647821, _a_(647818, _n_(647817, "p", lambda: p), "map"), _n_(647819, "get_api_item", lambda: get_api_item), _n_(647820, "date_list", lambda: date_list))
    _l_(647822)
    _c_(647825, _a_(647824, _n_(647823, "p", lambda: p), "terminate"))
    _l_(647826)
    _c_(647829, _a_(647828, _n_(647827, "p", lambda: p), "join"))
    _l_(647830)

result = _c_(647835, _a_(647833, _n_(647832, "pd", lambda: pd), "concat"), _n_(647834, "results", lambda: results))
_l_(647836)