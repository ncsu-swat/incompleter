# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import collections as clt
    _l_(87019)

except ImportError:
    pass

def check_break_list(nums, n):
    _l_(87050)

    coll_data = _c_(87023, _a_(87021, _n_(87020, "clt", lambda: clt), "Counter"), _n_(87022, "nums", lambda: nums))
    _l_(87024)
    for x in _c_(87029, _n_(87025, "sorted", lambda: sorted), _c_(87028, _a_(87027, _n_(87026, "coll_data", lambda: coll_data), "keys"))):
        _l_(87048)

        for index in _c_(87032, _n_(87030, "range", lambda: range), 1, _n_(87031, "n", lambda: n)):
            _l_(87047)

            _n_(87033, "coll_data", lambda: coll_data)[_n_(87034, "x", lambda: x) + _n_(87035, "index", lambda: index)] = _n_(87036, "coll_data", lambda: coll_data)[_n_(87037, "x", lambda: x) + _n_(87038, "index", lambda: index)] - _n_(87039, "coll_data", lambda: coll_data)[_n_(87040, "x", lambda: x)]
            _l_(87041)
            if _n_(87042, "coll_data", lambda: coll_data)[_n_(87043, "x", lambda: x) + _n_(87044, "index", lambda: index)] < 0:
                _l_(87046)

                aux = False
                _l_(87045)
                return aux
    aux = True
    _l_(87049)
    return aux
nums = [1, 2, 3, 4, 5, 6, 7, 8]
_l_(87051)
n = 4
_l_(87052)
_c_(87055, _n_(87053, "print", lambda: print), 'Original list:', _n_(87054, "nums", lambda: nums))
_l_(87056)
_c_(87059, _n_(87057, "print", lambda: print), 'Number to devide the said list:', _n_(87058, "n", lambda: n))
_l_(87060)
_c_(87066, _n_(87061, "print", lambda: print), _c_(87065, _n_(87062, "check_break_list", lambda: check_break_list), _n_(87063, "nums", lambda: nums), _n_(87064, "n", lambda: n)))
_l_(87067)
nums = [1, 2, 3, 4, 5, 6, 7, 8]
_l_(87068)
_c_(87071, _n_(87069, "print", lambda: print), '\nOriginal list:', _n_(87070, "nums", lambda: nums))
_l_(87072)
_c_(87075, _n_(87073, "print", lambda: print), 'Number to devide the said list:', _n_(87074, "n", lambda: n))
_l_(87076)
_c_(87082, _n_(87077, "print", lambda: print), _c_(87081, _n_(87078, "check_break_list", lambda: check_break_list), _n_(87079, "nums", lambda: nums), _n_(87080, "n", lambda: n)))
_l_(87083)