# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import collections as clt
    _l_(86891)

except ImportError:
    pass

def check_break_list(nums, n):
    _l_(86922)

    coll_data = _c_(86895, _a_(86893, _n_(86892, "clt", lambda: clt), "Counter"), _n_(86894, "nums", lambda: nums))
    _l_(86896)
    for x in _c_(86901, _n_(86897, "sorted", lambda: sorted), _c_(86900, _a_(86899, _n_(86898, "coll_data", lambda: coll_data), "keys"))):
        _l_(86920)

        for index in _c_(86904, _n_(86902, "range", lambda: range), 1, _n_(86903, "n", lambda: n)):
            _l_(86919)

            _n_(86905, "coll_data", lambda: coll_data)[_n_(86906, "x", lambda: x) + _n_(86907, "index", lambda: index)] = _n_(86908, "coll_data", lambda: coll_data)[_n_(86909, "x", lambda: x) + _n_(86910, "index", lambda: index)] - _n_(86911, "coll_data", lambda: coll_data)[_n_(86912, "x", lambda: x)]
            _l_(86913)
            if _n_(86914, "coll_data", lambda: coll_data)[_n_(86915, "x", lambda: x) + _n_(86916, "index", lambda: index)] < 0:
                _l_(86918)

                aux = False
                _l_(86917)
                return aux
    aux = True
    _l_(86921)
    return aux
nums = [1, 2, 3, 4, 5, 6, 7, 8]
_l_(86923)
n = 4
_l_(86924)
_c_(86927, _n_(86925, "print", lambda: print), 'Original list:', _n_(86926, "nums", lambda: nums))
_l_(86928)
_c_(86931, _n_(86929, "print", lambda: print), 'Number to devide the said list:', _n_(86930, "n", lambda: n))
_l_(86932)
_c_(86938, _n_(86933, "print", lambda: print), _c_(86937, _n_(86934, "check_break_list", lambda: check_break_list), _n_(86935, "nums", lambda: nums), _n_(86936, "n", lambda: n)))
_l_(86939)
n = 3
_l_(86940)
_c_(86943, _n_(86941, "print", lambda: print), '\nOriginal list:', _n_(86942, "nums", lambda: nums))
_l_(86944)
_c_(86947, _n_(86945, "print", lambda: print), 'Number to devide the said list:', _n_(86946, "n", lambda: n))
_l_(86948)
_c_(86954, _n_(86949, "print", lambda: print), _c_(86953, _n_(86950, "check_break_list", lambda: check_break_list), _n_(86951, "nums", lambda: nums), _n_(86952, "n", lambda: n)))
_l_(86955)