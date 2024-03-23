# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import itertools
    _l_(40881)

except ImportError:
    pass

def combination(str1):
    _l_(40900)

    result = _c_(40894, _n_(40882, "map", lambda: map), _a_(40883, '', "join"), _c_(40893, _a_(40885, _n_(40884, "itertools", lambda: itertools), "product"), *((_c_(40888, _a_(40887, _n_(40886, "c", lambda: c), "lower")), _c_(40891, _a_(40890, _n_(40889, "c", lambda: c), "upper"))) for c in _n_(40892, "str1", lambda: str1))))
    _l_(40895)
    aux = _c_(40898, _n_(40896, "list", lambda: list), _n_(40897, "result", lambda: result))
    _l_(40899)
    return aux
st = 'abc'
_l_(40901)
_c_(40903, _n_(40902, "print", lambda: print), 'Original string:')
_l_(40904)
_c_(40907, _n_(40905, "print", lambda: print), _n_(40906, "st", lambda: st))
_l_(40908)
_c_(40910, _n_(40909, "print", lambda: print), 'All lower and upper mixed case combinations of the said string:')
_l_(40911)
_c_(40916, _n_(40912, "print", lambda: print), _c_(40915, _n_(40913, "combination", lambda: combination), _n_(40914, "st", lambda: st)))
_l_(40917)
st = 'w3r'
_l_(40918)
_c_(40920, _n_(40919, "print", lambda: print), '\nOriginal string:')
_l_(40921)
_c_(40924, _n_(40922, "print", lambda: print), _n_(40923, "st", lambda: st))
_l_(40925)
_c_(40927, _n_(40926, "print", lambda: print), 'All lower and upper mixed case combinations of the said string:')
_l_(40928)
_c_(40933, _n_(40929, "print", lambda: print), _c_(40932, _n_(40930, "combination", lambda: combination), _n_(40931, "st", lambda: st)))
_l_(40934)
_c_(40936, _n_(40935, "print", lambda: print), '\nOriginal string:')
_l_(40937)
_c_(40940, _n_(40938, "print", lambda: print), _n_(40939, "st", lambda: st))
_l_(40941)
_c_(40943, _n_(40942, "print", lambda: print), 'All lower and upper mixed case combinations of the said string:')
_l_(40944)
_c_(40949, _n_(40945, "print", lambda: print), _c_(40948, _n_(40946, "combination", lambda: combination), _n_(40947, "st", lambda: st)))
_l_(40950)