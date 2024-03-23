# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def reverse_list_of_lists(nums, lr, hr):
    _l_(71337)

    temp = []
    _l_(71315)
    for (idx, el) in _c_(71318, _n_(71316, "enumerate", lambda: enumerate), _n_(71317, "nums", lambda: nums)):
        _l_(71329)

        if _n_(71319, "idx", lambda: idx) >= _n_(71320, "lr", lambda: lr) and _n_(71321, "idx", lambda: idx) < _n_(71322, "hr", lambda: hr):
            _l_(71328)

            _c_(71326, _a_(71324, _n_(71323, "temp", lambda: temp), "append"), _n_(71325, "el", lambda: el))
            _l_(71327)
    result_min = _c_(71332, _n_(71330, "min", lambda: min), _n_(71331, "temp", lambda: temp))
    _l_(71333)
    aux = (_n_(71334, "result_max", lambda: result_max), _n_(71335, "result_min", lambda: result_min))
    _l_(71336)
    return aux
nums = [4, 3, 0, 5, 3, 0, 2, 3, 4, 2, 4, 3, 5]
_l_(71338)
_c_(71340, _n_(71339, "print", lambda: print), 'Original list:')
_l_(71341)
_c_(71344, _n_(71342, "print", lambda: print), _n_(71343, "nums", lambda: nums))
_l_(71345)
_c_(71347, _n_(71346, "print", lambda: print), '\nIndex range:')
_l_(71348)
lr = 3
_l_(71349)
hr = 8
_l_(71350)
_c_(71354, _n_(71351, "print", lambda: print), _n_(71352, "lr", lambda: lr), 'to', _n_(71353, "hr", lambda: hr))
_l_(71355)
_c_(71357, _n_(71356, "print", lambda: print), '\nMaximum and minimum values of the said given list within index range:')
_l_(71358)
_c_(71365, _n_(71359, "print", lambda: print), _c_(71364, _n_(71360, "reverse_list_of_lists", lambda: reverse_list_of_lists), _n_(71361, "nums", lambda: nums), _n_(71362, "lr", lambda: lr), _n_(71363, "hr", lambda: hr)))
_l_(71366)