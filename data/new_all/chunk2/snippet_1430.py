# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59863756/python-typeerror-when-generating-a-list-of-dates
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from pandas.tseries import offsets
    _l_(470118)

except ImportError:
    pass

years = []
_l_(470119)
for i in  _c_(470121, _n_(470120, "range", lambda: range), 1990,2020):
    _l_(470130)

    _c_(470128, _a_(470126, _c_(470125, _a_(470123, _n_(470122, "offsets", lambda: offsets), "YearBegin"), _n_(470124, "years", lambda: years)), "append"), _n_(470127, "i", lambda: i))
    _l_(470129)