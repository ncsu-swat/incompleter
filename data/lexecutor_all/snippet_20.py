# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1436703/what-is-the-difference-between-str-and-repr
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import datetime
    _l_(1547985)

except ImportError:
    pass
today = _c_(1547989, _a_(1547988, _a_(1547987, _n_(1547986, "datetime", lambda: datetime), "datetime"), "now"))
_l_(1547990)
_c_(1547993, _n_(1547991, "str", lambda: str), _n_(1547992, "today", lambda: today))
_l_(1547994)
'2012-03-14 09:21:58.130922'
_l_(1547995)
_c_(1547998, _n_(1547996, "repr", lambda: repr), _n_(1547997, "today", lambda: today))
_l_(1547999)
'datetime.datetime(2012, 3, 14, 9, 21, 58, 130922)'
_l_(1548000)

