# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/45981145/inheriting-from-a-class-datetime-date-causes-a-super-init-too-many
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
FORMAT__DD_MM_YYYY = "dd.mm.yyyy"
_l_(382632)
try:
    from datetime import date
    _l_(382634)

except ImportError:
    pass


class DateExtended(_n_(382635, "date", lambda: date)):
    _l_(382663)

    date_string = None
    _l_(382636)
    date_format = None
    _l_(382637)

    def __init__(self, year: _n_(382638, "int", lambda: int), month: _n_(382639, "int", lambda: int), day: _n_(382640, "int", lambda: int), date_format: _n_(382641, "str", lambda: str)=None):
        _l_(382662)

        _c_(382647, _a_(382643, _n_(382642, "super", lambda: super)(), "__init__"), year=_n_(382644, "year", lambda: year), month=_n_(382645, "month", lambda: month), day=_n_(382646, "day", lambda: day))
        _l_(382648)
        _n_(382649, "self", lambda: self).date_format = _n_(382650, "date_format", lambda: date_format)
        _l_(382651)
        _n_(382652, "self", lambda: self).date_string = _c_(382660, _a_(382653, "{:02d}.{:02d}.{:04d}", "format"), _a_(382655, _n_(382654, "self", lambda: self), "day"), _a_(382657, _n_(382656, "self", lambda: self), "month"), _a_(382659, _n_(382658, "self", lambda: self), "year"))
        _l_(382661)

bla1 = _c_(382666, _n_(382664, "DateExtended", lambda: DateExtended), year=2010, month=5, day=3, date_format=_n_(382665, "FORMAT__DD_MM_YYYY_DOT", lambda: FORMAT__DD_MM_YYYY_DOT))
_l_(382667)