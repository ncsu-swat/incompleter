# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def quick_sort(nums: _n_(101656, "list", lambda: list)) -> _n_(101657, "list", lambda: list):
    _l_(101678)

    if _c_(101660, _n_(101658, "len", lambda: len), _n_(101659, "nums", lambda: nums)) <= 1:
        _l_(101677)

        aux = _n_(101661, "nums", lambda: nums)
        _l_(101662)
        return aux
    else:
        aux = _c_(101668, _n_(101663, "quick_sort", lambda: quick_sort), [_n_(101664, "el", lambda: el) for el in _n_(101665, "nums", lambda: nums)[1:] if _n_(101666, "el", lambda: el) <= _n_(101667, "nums", lambda: nums)[0]]) + [_n_(101669, "nums", lambda: nums)[0]] + _c_(101675, _n_(101670, "quick_sort", lambda: quick_sort), [_n_(101671, "el", lambda: el) for el in _n_(101672, "nums", lambda: nums)[1:] if _n_(101673, "el", lambda: el) > _n_(101674, "nums", lambda: nums)[0]])
        _l_(101676)
        return aux
_c_(101680, _n_(101679, "print", lambda: print), '\nOriginal list:')
_l_(101681)
_c_(101684, _n_(101682, "print", lambda: print), _n_(101683, "nums", lambda: nums))
_l_(101685)
_c_(101687, _n_(101686, "print", lambda: print), 'After applying Recursive Quick Sort the said list becomes:')
_l_(101688)
_c_(101693, _n_(101689, "print", lambda: print), _c_(101692, _n_(101690, "quick_sort", lambda: quick_sort), _n_(101691, "nums", lambda: nums)))
_l_(101694)
nums = [5, 9, 10, 3, -4, 5, 178, 92, 46, -18, 0, 7]
_l_(101695)
_c_(101697, _n_(101696, "print", lambda: print), '\nOriginal list:')
_l_(101698)
_c_(101701, _n_(101699, "print", lambda: print), _n_(101700, "nums", lambda: nums))
_l_(101702)
_c_(101704, _n_(101703, "print", lambda: print), 'After applying Recursive Quick Sort the said list becomes:')
_l_(101705)
_c_(101710, _n_(101706, "print", lambda: print), _c_(101709, _n_(101707, "quick_sort", lambda: quick_sort), _n_(101708, "nums", lambda: nums)))
_l_(101711)
nums = [1.1, 1, 0, -1, -1.1, 0.1]
_l_(101712)
_c_(101714, _n_(101713, "print", lambda: print), '\nOriginal list:')
_l_(101715)
_c_(101718, _n_(101716, "print", lambda: print), _n_(101717, "nums", lambda: nums))
_l_(101719)
_c_(101721, _n_(101720, "print", lambda: print), 'After applying Recursive Quick Sort the said list becomes:')
_l_(101722)
_c_(101727, _n_(101723, "print", lambda: print), _c_(101726, _n_(101724, "quick_sort", lambda: quick_sort), _n_(101725, "nums", lambda: nums)))
_l_(101728)