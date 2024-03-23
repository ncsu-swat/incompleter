# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def quick_sort(nums: _n_(8475, "list", lambda: list)) -> _n_(8476, "list", lambda: list):
    _l_(8497)

    if _c_(8479, _n_(8477, "len", lambda: len), _n_(8478, "nums", lambda: nums)) <= 1:
        _l_(8496)

        aux = _n_(8480, "nums", lambda: nums)
        _l_(8481)
        return aux
    else:
        aux = _c_(8487, _n_(8482, "quick_sort", lambda: quick_sort), [_n_(8483, "el", lambda: el) for el in _n_(8484, "nums", lambda: nums)[1:] if _n_(8485, "el", lambda: el) <= _n_(8486, "nums", lambda: nums)[0]]) + [_n_(8488, "nums", lambda: nums)[0]] + _c_(8494, _n_(8489, "quick_sort", lambda: quick_sort), [_n_(8490, "el", lambda: el) for el in _n_(8491, "nums", lambda: nums)[1:] if _n_(8492, "el", lambda: el) > _n_(8493, "nums", lambda: nums)[0]])
        _l_(8495)
        return aux
nums = [4, 3, 5, 1, 2]
_l_(8498)
_c_(8500, _n_(8499, "print", lambda: print), '\nOriginal list:')
_l_(8501)
_c_(8504, _n_(8502, "print", lambda: print), _n_(8503, "nums", lambda: nums))
_l_(8505)
_c_(8507, _n_(8506, "print", lambda: print), 'After applying Recursive Quick Sort the said list becomes:')
_l_(8508)
_c_(8513, _n_(8509, "print", lambda: print), _c_(8512, _n_(8510, "quick_sort", lambda: quick_sort), _n_(8511, "nums", lambda: nums)))
_l_(8514)
nums = [5, 9, 10, 3, -4, 5, 178, 92, 46, -18, 0, 7]
_l_(8515)
_c_(8517, _n_(8516, "print", lambda: print), '\nOriginal list:')
_l_(8518)
_c_(8521, _n_(8519, "print", lambda: print), _n_(8520, "nums", lambda: nums))
_l_(8522)
_c_(8524, _n_(8523, "print", lambda: print), 'After applying Recursive Quick Sort the said list becomes:')
_l_(8525)
_c_(8530, _n_(8526, "print", lambda: print), _c_(8529, _n_(8527, "quick_sort", lambda: quick_sort), _n_(8528, "nums", lambda: nums)))
_l_(8531)
_c_(8533, _n_(8532, "print", lambda: print), '\nOriginal list:')
_l_(8534)
_c_(8537, _n_(8535, "print", lambda: print), _n_(8536, "nums", lambda: nums))
_l_(8538)
_c_(8540, _n_(8539, "print", lambda: print), 'After applying Recursive Quick Sort the said list becomes:')
_l_(8541)
_c_(8546, _n_(8542, "print", lambda: print), _c_(8545, _n_(8543, "quick_sort", lambda: quick_sort), _n_(8544, "nums", lambda: nums)))
_l_(8547)