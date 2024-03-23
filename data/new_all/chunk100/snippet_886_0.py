# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import collections as clt
    _l_(86825)

except ImportError:
    pass

def check_break_list(nums, n):
    _l_(86856)

    coll_data = _c_(86829, _a_(86827, _n_(86826, "clt", lambda: clt), "Counter"), _n_(86828, "nums", lambda: nums))
    _l_(86830)
    for x in _c_(86835, _n_(86831, "sorted", lambda: sorted), _c_(86834, _a_(86833, _n_(86832, "coll_data", lambda: coll_data), "keys"))):
        _l_(86854)

        for index in _c_(86838, _n_(86836, "range", lambda: range), 1, _n_(86837, "n", lambda: n)):
            _l_(86853)

            _n_(86839, "coll_data", lambda: coll_data)[_n_(86840, "x", lambda: x) + _n_(86841, "index", lambda: index)] = _n_(86842, "coll_data", lambda: coll_data)[_n_(86843, "x", lambda: x) + _n_(86844, "index", lambda: index)] - _n_(86845, "coll_data", lambda: coll_data)[_n_(86846, "x", lambda: x)]
            _l_(86847)
            if _n_(86848, "coll_data", lambda: coll_data)[_n_(86849, "x", lambda: x) + _n_(86850, "index", lambda: index)] < 0:
                _l_(86852)

                aux = False
                _l_(86851)
                return aux
    aux = True
    _l_(86855)
    return aux
n = 4
_l_(86857)
_c_(86860, _n_(86858, "print", lambda: print), 'Original list:', _n_(86859, "nums", lambda: nums))
_l_(86861)
_c_(86864, _n_(86862, "print", lambda: print), 'Number to devide the said list:', _n_(86863, "n", lambda: n))
_l_(86865)
_c_(86871, _n_(86866, "print", lambda: print), _c_(86870, _n_(86867, "check_break_list", lambda: check_break_list), _n_(86868, "nums", lambda: nums), _n_(86869, "n", lambda: n)))
_l_(86872)
nums = [1, 2, 3, 4, 5, 6, 7, 8]
_l_(86873)
n = 3
_l_(86874)
_c_(86877, _n_(86875, "print", lambda: print), '\nOriginal list:', _n_(86876, "nums", lambda: nums))
_l_(86878)
_c_(86881, _n_(86879, "print", lambda: print), 'Number to devide the said list:', _n_(86880, "n", lambda: n))
_l_(86882)
_c_(86888, _n_(86883, "print", lambda: print), _c_(86887, _n_(86884, "check_break_list", lambda: check_break_list), _n_(86885, "nums", lambda: nums), _n_(86886, "n", lambda: n)))
_l_(86889)