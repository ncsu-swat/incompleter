# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def reverse_list_of_lists(nums, lr, hr):
    _l_(71558)

    temp = []
    _l_(71532)
    for (idx, el) in _c_(71535, _n_(71533, "enumerate", lambda: enumerate), _n_(71534, "nums", lambda: nums)):
        _l_(71546)

        if _n_(71536, "idx", lambda: idx) >= _n_(71537, "lr", lambda: lr) and _n_(71538, "idx", lambda: idx) < _n_(71539, "hr", lambda: hr):
            _l_(71545)

            _c_(71543, _a_(71541, _n_(71540, "temp", lambda: temp), "append"), _n_(71542, "el", lambda: el))
            _l_(71544)
    result_max = _c_(71549, _n_(71547, "max", lambda: max), _n_(71548, "temp", lambda: temp))
    _l_(71550)
    result_min = _c_(71553, _n_(71551, "min", lambda: min), _n_(71552, "temp", lambda: temp))
    _l_(71554)
    aux = (_n_(71555, "result_max", lambda: result_max), _n_(71556, "result_min", lambda: result_min))
    _l_(71557)
    return aux
nums = [4, 3, 0, 5, 3, 0, 2, 3, 4, 2, 4, 3, 5]
_l_(71559)
_c_(71561, _n_(71560, "print", lambda: print), 'Original list:')
_l_(71562)
_c_(71565, _n_(71563, "print", lambda: print), _n_(71564, "nums", lambda: nums))
_l_(71566)
_c_(71568, _n_(71567, "print", lambda: print), '\nIndex range:')
_l_(71569)
hr = 8
_l_(71570)
_c_(71574, _n_(71571, "print", lambda: print), _n_(71572, "lr", lambda: lr), 'to', _n_(71573, "hr", lambda: hr))
_l_(71575)
_c_(71577, _n_(71576, "print", lambda: print), '\nMaximum and minimum values of the said given list within index range:')
_l_(71578)
_c_(71585, _n_(71579, "print", lambda: print), _c_(71584, _n_(71580, "reverse_list_of_lists", lambda: reverse_list_of_lists), _n_(71581, "nums", lambda: nums), _n_(71582, "lr", lambda: lr), _n_(71583, "hr", lambda: hr)))
_l_(71586)