# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59589155/typeerror-unhashable-type-list-when-plotting-multiple-charts
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import fxcmpy
    _l_(473431)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(473433)

except ImportError:
    pass
try:
    from pandas import datetime
    _l_(473435)

except ImportError:
    pass
try:
    from pandas import DataFrame as df
    _l_(473437)

except ImportError:
    pass
try:
    import matplotlib
    _l_(473439)

except ImportError:
    pass
try:
    from pandas_datareader import data as web
    _l_(473441)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(473443)

except ImportError:
    pass
try:
    import datetime
    _l_(473445)

except ImportError:
    pass
try:
    from datetime import date
    _l_(473447)

except ImportError:
    pass
try:
    import numpy as np
    _l_(473449)

except ImportError:
    pass
TOKEN = "hidden "
_l_(473450)
con = _c_(473454, _a_(473452, _n_(473451, "fxcmpy", lambda: fxcmpy), "fxcmpy"), access_token=_n_(473453, "TOKEN", lambda: TOKEN), log_level='error')
_l_(473455)
_c_(473460, _n_(473456, "print", lambda: print), _c_(473459, _a_(473458, _n_(473457, "con", lambda: con), "get_instruments")))
_l_(473461)
ticker= _c_(473464, _a_(473463, _n_(473462, "con", lambda: con), "get_instruments"))
_l_(473465)
def convert(ticker):
    _l_(473470)

    aux = _c_(473468, _n_(473466, "tuple", lambda: tuple), _n_(473467, "ticker", lambda: ticker))
    _l_(473469)
    return aux
ticker = _c_(473473, _n_(473471, "convert", lambda: convert), _n_(473472, "ticker", lambda: ticker))
_l_(473474)
start = _c_(473477, _a_(473476, _n_(473475, "datetime", lambda: datetime), "datetime"), 2008,1,1)
_l_(473478)
end = _c_(473482, _a_(473481, _a_(473480, _n_(473479, "datetime", lambda: datetime), "datetime"), "today"))
_l_(473483)
today = _c_(473486, _a_(473485, _n_(473484, "date", lambda: date), "today"))
_l_(473487)
data = _c_(473493, _a_(473489, _n_(473488, "con", lambda: con), "get_candles"), _n_(473490, "ticker", lambda: ticker), period='D1', start = _n_(473491, "start", lambda: start), end = _n_(473492, "end", lambda: end))
_l_(473494)
_n_(473495, "data", lambda: data).index = _c_(473500, _a_(473497, _n_(473496, "pd", lambda: pd), "to_datetime"), _a_(473499, _n_(473498, "data", lambda: data), "index"), format ='%Y-%m-%d')
_l_(473501)