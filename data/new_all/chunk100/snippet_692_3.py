# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def reverse_list_of_lists(nums, lr, hr):
    _l_(71503)

    temp = []
    _l_(71477)
    for (idx, el) in _c_(71480, _n_(71478, "enumerate", lambda: enumerate), _n_(71479, "nums", lambda: nums)):
        _l_(71491)

        if _n_(71481, "idx", lambda: idx) >= _n_(71482, "lr", lambda: lr) and _n_(71483, "idx", lambda: idx) < _n_(71484, "hr", lambda: hr):
            _l_(71490)

            _c_(71488, _a_(71486, _n_(71485, "temp", lambda: temp), "append"), _n_(71487, "el", lambda: el))
            _l_(71489)
    result_max = _c_(71494, _n_(71492, "max", lambda: max), _n_(71493, "temp", lambda: temp))
    _l_(71495)
    result_min = _c_(71498, _n_(71496, "min", lambda: min), _n_(71497, "temp", lambda: temp))
    _l_(71499)
    aux = (_n_(71500, "result_max", lambda: result_max), _n_(71501, "result_min", lambda: result_min))
    _l_(71502)
    return aux
_c_(71505, _n_(71504, "print", lambda: print), 'Original list:')
_l_(71506)
_c_(71509, _n_(71507, "print", lambda: print), _n_(71508, "nums", lambda: nums))
_l_(71510)
_c_(71512, _n_(71511, "print", lambda: print), '\nIndex range:')
_l_(71513)
lr = 3
_l_(71514)
hr = 8
_l_(71515)
_c_(71519, _n_(71516, "print", lambda: print), _n_(71517, "lr", lambda: lr), 'to', _n_(71518, "hr", lambda: hr))
_l_(71520)
_c_(71522, _n_(71521, "print", lambda: print), '\nMaximum and minimum values of the said given list within index range:')
_l_(71523)
_c_(71530, _n_(71524, "print", lambda: print), _c_(71529, _n_(71525, "reverse_list_of_lists", lambda: reverse_list_of_lists), _n_(71526, "nums", lambda: nums), _n_(71527, "lr", lambda: lr), _n_(71528, "hr", lambda: hr)))
_l_(71531)