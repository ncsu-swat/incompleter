# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def reverse_list_of_lists(nums, lr, hr):
    _l_(71447)

    for (idx, el) in _c_(71424, _n_(71422, "enumerate", lambda: enumerate), _n_(71423, "nums", lambda: nums)):
        _l_(71435)

        if _n_(71425, "idx", lambda: idx) >= _n_(71426, "lr", lambda: lr) and _n_(71427, "idx", lambda: idx) < _n_(71428, "hr", lambda: hr):
            _l_(71434)

            _c_(71432, _a_(71430, _n_(71429, "temp", lambda: temp), "append"), _n_(71431, "el", lambda: el))
            _l_(71433)
    result_max = _c_(71438, _n_(71436, "max", lambda: max), _n_(71437, "temp", lambda: temp))
    _l_(71439)
    result_min = _c_(71442, _n_(71440, "min", lambda: min), _n_(71441, "temp", lambda: temp))
    _l_(71443)
    aux = (_n_(71444, "result_max", lambda: result_max), _n_(71445, "result_min", lambda: result_min))
    _l_(71446)
    return aux
nums = [4, 3, 0, 5, 3, 0, 2, 3, 4, 2, 4, 3, 5]
_l_(71448)
_c_(71450, _n_(71449, "print", lambda: print), 'Original list:')
_l_(71451)
_c_(71454, _n_(71452, "print", lambda: print), _n_(71453, "nums", lambda: nums))
_l_(71455)
_c_(71457, _n_(71456, "print", lambda: print), '\nIndex range:')
_l_(71458)
lr = 3
_l_(71459)
hr = 8
_l_(71460)
_c_(71464, _n_(71461, "print", lambda: print), _n_(71462, "lr", lambda: lr), 'to', _n_(71463, "hr", lambda: hr))
_l_(71465)
_c_(71467, _n_(71466, "print", lambda: print), '\nMaximum and minimum values of the said given list within index range:')
_l_(71468)
_c_(71475, _n_(71469, "print", lambda: print), _c_(71474, _n_(71470, "reverse_list_of_lists", lambda: reverse_list_of_lists), _n_(71471, "nums", lambda: nums), _n_(71472, "lr", lambda: lr), _n_(71473, "hr", lambda: hr)))
_l_(71476)