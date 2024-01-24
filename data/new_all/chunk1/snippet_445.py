# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/46209731/typeerror-strptime-argument-1-must-be-str-not-float
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(384979)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(384981)

except ImportError:
    pass
try:
    from datetime import datetime as dt
    _l_(384983)

except ImportError:
    pass

data0 = _c_(384986, _a_(384985, _n_(384984, "pd", lambda: pd), "read_csv"), '2009-10.csv')
_l_(384987)
data1 = _c_(384990, _a_(384989, _n_(384988, "pd", lambda: pd), "read_csv"), '2010-11.csv')
_l_(384991)

def parse_date(date):
    _l_(385002)

    if _n_(384992, "date", lambda: date) == '':
        _l_(385001)

        aux = None
        _l_(384993)
        return aux
    else:
        aux = _c_(384999, _a_(384998, _c_(384997, _a_(384995, _n_(384994, "dt", lambda: dt), "strptime"), _n_(384996, "date", lambda: date), '%d/%m/%y'), "date"))
        _l_(385000)
        return aux

_n_(385003, "data0", lambda: data0).Date = _c_(385008, _a_(385006, _a_(385005, _n_(385004, "data0", lambda: data0), "Date"), "apply"), _n_(385007, "parse_date", lambda: parse_date))
_l_(385009)
_n_(385010, "data1", lambda: data1).Date = _c_(385015, _a_(385013, _a_(385012, _n_(385011, "data1", lambda: data1), "Date"), "apply"), _n_(385014, "parse_date", lambda: parse_date))
_l_(385016)