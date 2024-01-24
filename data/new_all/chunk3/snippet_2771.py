# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63841876/typeerror-list-object-is-not-an-iterator-tensorflow-custom-metric-callback
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
iter_val_data = _c_(540422, _n_(540419, "iter", lambda: iter), _a_(540421, _n_(540420, "self", lambda: self), "validation_data"))
_l_(540423)
for batch in _c_(540426, _n_(540424, "range", lambda: range), _n_(540425, "batches", lambda: batches)):
    _l_(540435)

    xVal = _c_(540429, _n_(540427, "next", lambda: next), _n_(540428, "iter_val_data", lambda: iter_val_data))
    _l_(540430)
    yVal = _c_(540433, _n_(540431, "next", lambda: next), _n_(540432, "iter_val_data", lambda: iter_val_data))
    _l_(540434)