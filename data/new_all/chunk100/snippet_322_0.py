# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def cocktail_shaker_sort(nums):
    _l_(31084)

    for i in _c_(31039, _n_(31035, "range", lambda: range), _c_(31038, _n_(31036, "len", lambda: len), _n_(31037, "nums", lambda: nums)) - 1, 0, -1):
        _l_(31083)

        is_swapped = False
        _l_(31040)
        for j in _c_(31043, _n_(31041, "range", lambda: range), _n_(31042, "i", lambda: i), 0, -1):
            _l_(31059)

            if _n_(31044, "nums", lambda: nums)[_n_(31045, "j", lambda: j)] < _n_(31046, "nums", lambda: nums)[_n_(31047, "j", lambda: j) - 1]:
                _l_(31058)

                (_n_(31048, "nums", lambda: nums)[_n_(31049, "j", lambda: j)], _n_(31050, "nums", lambda: nums)[_n_(31051, "j", lambda: j) - 1]) = (_n_(31052, "nums", lambda: nums)[_n_(31053, "j", lambda: j) - 1], _n_(31054, "nums", lambda: nums)[_n_(31055, "j", lambda: j)])
                _l_(31056)
                is_swapped = True
                _l_(31057)
        for j in _c_(31062, _n_(31060, "range", lambda: range), _n_(31061, "i", lambda: i)):
            _l_(31078)

            if _n_(31063, "nums", lambda: nums)[_n_(31064, "j", lambda: j)] > _n_(31065, "nums", lambda: nums)[_n_(31066, "j", lambda: j) + 1]:
                _l_(31077)

                (_n_(31067, "nums", lambda: nums)[_n_(31068, "j", lambda: j)], _n_(31069, "nums", lambda: nums)[_n_(31070, "j", lambda: j) + 1]) = (_n_(31071, "nums", lambda: nums)[_n_(31072, "j", lambda: j) + 1], _n_(31073, "nums", lambda: nums)[_n_(31074, "j", lambda: j)])
                _l_(31075)
                is_swapped = True
                _l_(31076)
        if not _n_(31079, "is_swapped", lambda: is_swapped):
            _l_(31082)

            aux = _n_(31080, "nums", lambda: nums)
            _l_(31081)
            return aux
num1 = _c_(31088, _a_(31087, _c_(31086, _n_(31085, "input", lambda: input), 'Input comma separated numbers:\n'), "strip"))
_l_(31089)
_c_(31094, _n_(31090, "print", lambda: print), _c_(31093, _n_(31091, "cocktail_shaker_sort", lambda: cocktail_shaker_sort), _n_(31092, "nums", lambda: nums)))
_l_(31095)