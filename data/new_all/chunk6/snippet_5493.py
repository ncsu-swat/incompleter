# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/77385362/i-cant-sum-the-numbers-of-a-nested-loop-typeerror-float-object-cannot-be-in
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
values = [29, 24, 20, 28, 22, 22, 23]
_l_(372620)
average = _c_(372623, _n_(372621, "sum", lambda: sum), _n_(372622, "values", lambda: values)) / _c_(372626, _n_(372624, "len", lambda: len), _n_(372625, "values", lambda: values))
_l_(372627)

for single_value in _n_(372628, "values", lambda: values):
    _l_(372642)

    values_subtraction_average = _n_(372629, "single_value", lambda: single_value) - _n_(372630, "average", lambda: average)
    _l_(372631)
    # >>> 5.0, 0.0, -4.0, 4.0, -2.0, -2.0, -1.0.

    for item in _c_(372634, _n_(372632, "range", lambda: range), _n_(372633, "values_subtraction_average", lambda: values_subtraction_average)):
        _l_(372641)

        x = _c_(372639, _n_(372635, "sum", lambda: sum), _c_(372638, _n_(372636, "float", lambda: float), _n_(372637, "item", lambda: item)))
        _l_(372640)