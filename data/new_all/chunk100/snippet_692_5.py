# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def reverse_list_of_lists(nums, lr, hr):
    _l_(71609)

    temp = []
    _l_(71587)
    for (idx, el) in _c_(71590, _n_(71588, "enumerate", lambda: enumerate), _n_(71589, "nums", lambda: nums)):
        _l_(71601)

        if _n_(71591, "idx", lambda: idx) >= _n_(71592, "lr", lambda: lr) and _n_(71593, "idx", lambda: idx) < _n_(71594, "hr", lambda: hr):
            _l_(71600)

            _c_(71598, _a_(71596, _n_(71595, "temp", lambda: temp), "append"), _n_(71597, "el", lambda: el))
            _l_(71599)
    result_max = _c_(71604, _n_(71602, "max", lambda: max), _n_(71603, "temp", lambda: temp))
    _l_(71605)
    aux = (_n_(71606, "result_max", lambda: result_max), _n_(71607, "result_min", lambda: result_min))
    _l_(71608)
    return aux
nums = [4, 3, 0, 5, 3, 0, 2, 3, 4, 2, 4, 3, 5]
_l_(71610)
_c_(71612, _n_(71611, "print", lambda: print), 'Original list:')
_l_(71613)
_c_(71616, _n_(71614, "print", lambda: print), _n_(71615, "nums", lambda: nums))
_l_(71617)
_c_(71619, _n_(71618, "print", lambda: print), '\nIndex range:')
_l_(71620)
lr = 3
_l_(71621)
hr = 8
_l_(71622)
_c_(71626, _n_(71623, "print", lambda: print), _n_(71624, "lr", lambda: lr), 'to', _n_(71625, "hr", lambda: hr))
_l_(71627)
_c_(71629, _n_(71628, "print", lambda: print), '\nMaximum and minimum values of the said given list within index range:')
_l_(71630)
_c_(71637, _n_(71631, "print", lambda: print), _c_(71636, _n_(71632, "reverse_list_of_lists", lambda: reverse_list_of_lists), _n_(71633, "nums", lambda: nums), _n_(71634, "lr", lambda: lr), _n_(71635, "hr", lambda: hr)))
_l_(71638)