# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import collections as clt
    _l_(87085)

except ImportError:
    pass

def check_break_list(nums, n):
    _l_(87116)

    coll_data = _c_(87089, _a_(87087, _n_(87086, "clt", lambda: clt), "Counter"), _n_(87088, "nums", lambda: nums))
    _l_(87090)
    for x in _c_(87095, _n_(87091, "sorted", lambda: sorted), _c_(87094, _a_(87093, _n_(87092, "coll_data", lambda: coll_data), "keys"))):
        _l_(87114)

        for index in _c_(87098, _n_(87096, "range", lambda: range), 1, _n_(87097, "n", lambda: n)):
            _l_(87113)

            _n_(87099, "coll_data", lambda: coll_data)[_n_(87100, "x", lambda: x) + _n_(87101, "index", lambda: index)] = _n_(87102, "coll_data", lambda: coll_data)[_n_(87103, "x", lambda: x) + _n_(87104, "index", lambda: index)] - _n_(87105, "coll_data", lambda: coll_data)[_n_(87106, "x", lambda: x)]
            _l_(87107)
            if _n_(87108, "coll_data", lambda: coll_data)[_n_(87109, "x", lambda: x) + _n_(87110, "index", lambda: index)] < 0:
                _l_(87112)

                aux = False
                _l_(87111)
                return aux
    aux = True
    _l_(87115)
    return aux
nums = [1, 2, 3, 4, 5, 6, 7, 8]
_l_(87117)
_c_(87120, _n_(87118, "print", lambda: print), 'Original list:', _n_(87119, "nums", lambda: nums))
_l_(87121)
_c_(87124, _n_(87122, "print", lambda: print), 'Number to devide the said list:', _n_(87123, "n", lambda: n))
_l_(87125)
_c_(87131, _n_(87126, "print", lambda: print), _c_(87130, _n_(87127, "check_break_list", lambda: check_break_list), _n_(87128, "nums", lambda: nums), _n_(87129, "n", lambda: n)))
_l_(87132)
nums = [1, 2, 3, 4, 5, 6, 7, 8]
_l_(87133)
n = 3
_l_(87134)
_c_(87137, _n_(87135, "print", lambda: print), '\nOriginal list:', _n_(87136, "nums", lambda: nums))
_l_(87138)
_c_(87141, _n_(87139, "print", lambda: print), 'Number to devide the said list:', _n_(87140, "n", lambda: n))
_l_(87142)
_c_(87148, _n_(87143, "print", lambda: print), _c_(87147, _n_(87144, "check_break_list", lambda: check_break_list), _n_(87145, "nums", lambda: nums), _n_(87146, "n", lambda: n)))
_l_(87149)