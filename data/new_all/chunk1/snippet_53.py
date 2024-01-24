# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58168488/type-hint-returns-nameerror-name-datetime-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def time_in_range(start: _n_(413829, "datetime", lambda: datetime), end: _n_(413830, "datetime", lambda: datetime), x: _n_(413831, "datetime", lambda: datetime)) -> _n_(413832, "bool", lambda: bool):
    _l_(413845)

    """Return true if x is in the range [start, end]"""
    if _n_(413833, "start", lambda: start) <= _n_(413834, "end", lambda: end):
        _l_(413844)

        aux = _n_(413835, "start", lambda: start) <= _n_(413836, "x", lambda: x) <= _n_(413837, "end", lambda: end)
        _l_(413838)
        return aux
    else:
        aux = _n_(413839, "start", lambda: start) <= _n_(413840, "x", lambda: x) or _n_(413841, "x", lambda: x) <= _n_(413842, "end", lambda: end)
        _l_(413843)
        return aux