# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def reverse_list_of_lists(nums, lr, hr):
    _l_(71393)

    temp = []
    _l_(71367)
    for (idx, el) in _c_(71370, _n_(71368, "enumerate", lambda: enumerate), _n_(71369, "nums", lambda: nums)):
        _l_(71381)

        if _n_(71371, "idx", lambda: idx) >= _n_(71372, "lr", lambda: lr) and _n_(71373, "idx", lambda: idx) < _n_(71374, "hr", lambda: hr):
            _l_(71380)

            _c_(71378, _a_(71376, _n_(71375, "temp", lambda: temp), "append"), _n_(71377, "el", lambda: el))
            _l_(71379)
    result_max = _c_(71384, _n_(71382, "max", lambda: max), _n_(71383, "temp", lambda: temp))
    _l_(71385)
    result_min = _c_(71388, _n_(71386, "min", lambda: min), _n_(71387, "temp", lambda: temp))
    _l_(71389)
    aux = (_n_(71390, "result_max", lambda: result_max), _n_(71391, "result_min", lambda: result_min))
    _l_(71392)
    return aux
nums = [4, 3, 0, 5, 3, 0, 2, 3, 4, 2, 4, 3, 5]
_l_(71394)
_c_(71396, _n_(71395, "print", lambda: print), 'Original list:')
_l_(71397)
_c_(71400, _n_(71398, "print", lambda: print), _n_(71399, "nums", lambda: nums))
_l_(71401)
_c_(71403, _n_(71402, "print", lambda: print), '\nIndex range:')
_l_(71404)
lr = 3
_l_(71405)
_c_(71409, _n_(71406, "print", lambda: print), _n_(71407, "lr", lambda: lr), 'to', _n_(71408, "hr", lambda: hr))
_l_(71410)
_c_(71412, _n_(71411, "print", lambda: print), '\nMaximum and minimum values of the said given list within index range:')
_l_(71413)
_c_(71420, _n_(71414, "print", lambda: print), _c_(71419, _n_(71415, "reverse_list_of_lists", lambda: reverse_list_of_lists), _n_(71416, "nums", lambda: nums), _n_(71417, "lr", lambda: lr), _n_(71418, "hr", lambda: hr)))
_l_(71421)