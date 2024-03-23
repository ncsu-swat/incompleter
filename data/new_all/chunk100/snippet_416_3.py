# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import itertools
    _l_(40952)

except ImportError:
    pass

def combination(str1):
    _l_(40971)

    result = _c_(40965, _n_(40953, "map", lambda: map), _a_(40954, '', "join"), _c_(40964, _a_(40956, _n_(40955, "itertools", lambda: itertools), "product"), *((_c_(40959, _a_(40958, _n_(40957, "c", lambda: c), "lower")), _c_(40962, _a_(40961, _n_(40960, "c", lambda: c), "upper"))) for c in _n_(40963, "str1", lambda: str1))))
    _l_(40966)
    aux = _c_(40969, _n_(40967, "list", lambda: list), _n_(40968, "result", lambda: result))
    _l_(40970)
    return aux
st = 'abc'
_l_(40972)
_c_(40974, _n_(40973, "print", lambda: print), 'Original string:')
_l_(40975)
_c_(40978, _n_(40976, "print", lambda: print), _n_(40977, "st", lambda: st))
_l_(40979)
_c_(40981, _n_(40980, "print", lambda: print), 'All lower and upper mixed case combinations of the said string:')
_l_(40982)
_c_(40987, _n_(40983, "print", lambda: print), _c_(40986, _n_(40984, "combination", lambda: combination), _n_(40985, "st", lambda: st)))
_l_(40988)
_c_(40990, _n_(40989, "print", lambda: print), '\nOriginal string:')
_l_(40991)
_c_(40994, _n_(40992, "print", lambda: print), _n_(40993, "st", lambda: st))
_l_(40995)
_c_(40997, _n_(40996, "print", lambda: print), 'All lower and upper mixed case combinations of the said string:')
_l_(40998)
_c_(41003, _n_(40999, "print", lambda: print), _c_(41002, _n_(41000, "combination", lambda: combination), _n_(41001, "st", lambda: st)))
_l_(41004)
st = 'Python'
_l_(41005)
_c_(41007, _n_(41006, "print", lambda: print), '\nOriginal string:')
_l_(41008)
_c_(41011, _n_(41009, "print", lambda: print), _n_(41010, "st", lambda: st))
_l_(41012)
_c_(41014, _n_(41013, "print", lambda: print), 'All lower and upper mixed case combinations of the said string:')
_l_(41015)
_c_(41020, _n_(41016, "print", lambda: print), _c_(41019, _n_(41017, "combination", lambda: combination), _n_(41018, "st", lambda: st)))
_l_(41021)