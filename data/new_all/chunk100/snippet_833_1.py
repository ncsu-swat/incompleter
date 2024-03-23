# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from itertools import groupby
    _l_(83064)

except ImportError:
    pass

def count_same_pair(nums):
    _l_(83074)

    result = [_c_(83067, _n_(83065, "sum", lambda: sum), (1 for _ in _n_(83066, "group", lambda: group))) for (_, group) in _c_(83070, _n_(83068, "groupby", lambda: groupby), _n_(83069, "nums", lambda: nums))]
    _l_(83071)
    aux = _n_(83072, "result", lambda: result)
    _l_(83073)
    return aux
_c_(83076, _n_(83075, "print", lambda: print), 'Original lists:')
_l_(83077)
_c_(83080, _n_(83078, "print", lambda: print), _n_(83079, "nums", lambda: nums))
_l_(83081)
_c_(83083, _n_(83082, "print", lambda: print), '\nFrequency of the consecutive duplicate elements:')
_l_(83084)
_c_(83089, _n_(83085, "print", lambda: print), _c_(83088, _n_(83086, "count_same_pair", lambda: count_same_pair), _n_(83087, "nums", lambda: nums)))
_l_(83090)