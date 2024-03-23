# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def quick_sort(nums: _n_(8548, "list", lambda: list)) -> _n_(8549, "list", lambda: list):
    _l_(8570)

    if _c_(8552, _n_(8550, "len", lambda: len), _n_(8551, "nums", lambda: nums)) <= 1:
        _l_(8569)

        aux = _n_(8553, "nums", lambda: nums)
        _l_(8554)
        return aux
    else:
        aux = _c_(8560, _n_(8555, "quick_sort", lambda: quick_sort), [_n_(8556, "el", lambda: el) for el in _n_(8557, "nums", lambda: nums)[1:] if _n_(8558, "el", lambda: el) <= _n_(8559, "nums", lambda: nums)[0]]) + [_n_(8561, "nums", lambda: nums)[0]] + _c_(8567, _n_(8562, "quick_sort", lambda: quick_sort), [_n_(8563, "el", lambda: el) for el in _n_(8564, "nums", lambda: nums)[1:] if _n_(8565, "el", lambda: el) > _n_(8566, "nums", lambda: nums)[0]])
        _l_(8568)
        return aux
_c_(8572, _n_(8571, "print", lambda: print), '\nOriginal list:')
_l_(8573)
_c_(8576, _n_(8574, "print", lambda: print), _n_(8575, "nums", lambda: nums))
_l_(8577)
_c_(8579, _n_(8578, "print", lambda: print), 'After applying Recursive Quick Sort the said list becomes:')
_l_(8580)
_c_(8585, _n_(8581, "print", lambda: print), _c_(8584, _n_(8582, "quick_sort", lambda: quick_sort), _n_(8583, "nums", lambda: nums)))
_l_(8586)
nums = [5, 9, 10, 3, -4, 5, 178, 92, 46, -18, 0, 7]
_l_(8587)
_c_(8589, _n_(8588, "print", lambda: print), '\nOriginal list:')
_l_(8590)
_c_(8593, _n_(8591, "print", lambda: print), _n_(8592, "nums", lambda: nums))
_l_(8594)
_c_(8596, _n_(8595, "print", lambda: print), 'After applying Recursive Quick Sort the said list becomes:')
_l_(8597)
_c_(8602, _n_(8598, "print", lambda: print), _c_(8601, _n_(8599, "quick_sort", lambda: quick_sort), _n_(8600, "nums", lambda: nums)))
_l_(8603)
nums = [1.1, 1, 0, -1, -1.1, 0.1]
_l_(8604)
_c_(8606, _n_(8605, "print", lambda: print), '\nOriginal list:')
_l_(8607)
_c_(8610, _n_(8608, "print", lambda: print), _n_(8609, "nums", lambda: nums))
_l_(8611)
_c_(8613, _n_(8612, "print", lambda: print), 'After applying Recursive Quick Sort the said list becomes:')
_l_(8614)
_c_(8619, _n_(8615, "print", lambda: print), _c_(8618, _n_(8616, "quick_sort", lambda: quick_sort), _n_(8617, "nums", lambda: nums)))
_l_(8620)