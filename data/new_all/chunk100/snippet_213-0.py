# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def tuple_max_val(nums):
    _l_(105320)

    result_max = _c_(105307, _n_(105301, "max", lambda: max), [_c_(105305, _n_(105302, "abs", lambda: abs), _n_(105303, "x", lambda: x) * _n_(105304, "y", lambda: y)) for x, y in _n_(105306, "nums", lambda: nums)])
    _l_(105308)
    result_min = _c_(105315, _n_(105309, "min", lambda: min), [_c_(105313, _n_(105310, "abs", lambda: abs), _n_(105311, "x", lambda: x) * _n_(105312, "y", lambda: y)) for x, y in _n_(105314, "nums", lambda: nums)])
    _l_(105316)
    aux = (_n_(105317, "result_max", lambda: result_max), _n_(105318, "result_min", lambda: result_min))
    _l_(105319)
    return aux
_c_(105322, _n_(105321, "print", lambda: print), 'The original list, tuple : ')
_l_(105323)
_c_(105326, _n_(105324, "print", lambda: print), _n_(105325, "nums", lambda: nums))
_l_(105327)
_c_(105329, _n_(105328, "print", lambda: print), '\nMaximum and minimum product from the pairs of the said tuple of list:')
_l_(105330)
_c_(105335, _n_(105331, "print", lambda: print), _c_(105334, _n_(105332, "tuple_max_val", lambda: tuple_max_val), _n_(105333, "nums", lambda: nums)))
_l_(105336)