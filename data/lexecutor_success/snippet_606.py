# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1060279/iterating-through-a-range-of-dates-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from datetime import date,timedelta
    _l_(1538489)

except ImportError:
    pass
delta = _c_(1538491, _n_(1538490, "timedelta", lambda: timedelta), days=1)
_l_(1538492)
start = _c_(1538494, _n_(1538493, "date", lambda: date), 2020,1,1)
_l_(1538495)
end=_c_(1538497, _n_(1538496, "date", lambda: date), 2020,9,1)
_l_(1538498)
loop_date = _n_(1538499, "start", lambda: start)
_l_(1538500)
while _n_(1538501, "loop_date", lambda: loop_date)<=_n_(1538502, "end", lambda: end):
    _l_(1538509)

    _c_(1538505, _n_(1538503, "print", lambda: print), _n_(1538504, "loop_date", lambda: loop_date))
    _l_(1538506)
    loop_date+=_n_(1538507, "delta", lambda: delta)
    _l_(1538508)

