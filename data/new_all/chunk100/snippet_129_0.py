# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def quick_sort(nums: _n_(8402, "list", lambda: list)) -> _n_(8403, "list", lambda: list):
    _l_(8424)

    if _c_(8406, _n_(8404, "len", lambda: len), _n_(8405, "nums", lambda: nums)) <= 1:
        _l_(8423)

        aux = _n_(8407, "nums", lambda: nums)
        _l_(8408)
        return aux
    else:
        aux = _c_(8414, _n_(8409, "quick_sort", lambda: quick_sort), [_n_(8410, "el", lambda: el) for el in _n_(8411, "nums", lambda: nums)[1:] if _n_(8412, "el", lambda: el) <= _n_(8413, "nums", lambda: nums)[0]]) + [_n_(8415, "nums", lambda: nums)[0]] + _c_(8421, _n_(8416, "quick_sort", lambda: quick_sort), [_n_(8417, "el", lambda: el) for el in _n_(8418, "nums", lambda: nums)[1:] if _n_(8419, "el", lambda: el) > _n_(8420, "nums", lambda: nums)[0]])
        _l_(8422)
        return aux
nums = [4, 3, 5, 1, 2]
_l_(8425)
_c_(8427, _n_(8426, "print", lambda: print), '\nOriginal list:')
_l_(8428)
_c_(8431, _n_(8429, "print", lambda: print), _n_(8430, "nums", lambda: nums))
_l_(8432)
_c_(8434, _n_(8433, "print", lambda: print), 'After applying Recursive Quick Sort the said list becomes:')
_l_(8435)
_c_(8440, _n_(8436, "print", lambda: print), _c_(8439, _n_(8437, "quick_sort", lambda: quick_sort), _n_(8438, "nums", lambda: nums)))
_l_(8441)
_c_(8443, _n_(8442, "print", lambda: print), '\nOriginal list:')
_l_(8444)
_c_(8447, _n_(8445, "print", lambda: print), _n_(8446, "nums", lambda: nums))
_l_(8448)
_c_(8450, _n_(8449, "print", lambda: print), 'After applying Recursive Quick Sort the said list becomes:')
_l_(8451)
_c_(8456, _n_(8452, "print", lambda: print), _c_(8455, _n_(8453, "quick_sort", lambda: quick_sort), _n_(8454, "nums", lambda: nums)))
_l_(8457)
nums = [1.1, 1, 0, -1, -1.1, 0.1]
_l_(8458)
_c_(8460, _n_(8459, "print", lambda: print), '\nOriginal list:')
_l_(8461)
_c_(8464, _n_(8462, "print", lambda: print), _n_(8463, "nums", lambda: nums))
_l_(8465)
_c_(8467, _n_(8466, "print", lambda: print), 'After applying Recursive Quick Sort the said list becomes:')
_l_(8468)
_c_(8473, _n_(8469, "print", lambda: print), _c_(8472, _n_(8470, "quick_sort", lambda: quick_sort), _n_(8471, "nums", lambda: nums)))
_l_(8474)