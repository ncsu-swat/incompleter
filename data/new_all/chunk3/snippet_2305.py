# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/52671829/trying-to-split-a-string-but-i-keep-getting-this-error-type-error-must-be-str
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from random import *
    _l_(576957)

except ImportError:
    pass
number = _c_(576959, _n_(576958, "randint", lambda: randint), 1000,9999)
_l_(576960)
strnumber = _c_(576963, _n_(576961, "str", lambda: str), _n_(576962, "number", lambda: number))
_l_(576964)
a,b,c,d = _c_(576975, _a_(576966, _n_(576965, "strnumber", lambda: strnumber), "split"), [_n_(576967, "strnumber", lambda: strnumber)[_n_(576968, "i", lambda: i):_n_(576969, "i", lambda: i)+1] for i in _c_(576974, _n_(576970, "range", lambda: range), 0, _c_(576973, _n_(576971, "len", lambda: len), _n_(576972, "strnumber", lambda: strnumber)), 1)])
_l_(576976)
_c_(576979, _n_(576977, "print", lambda: print), _n_(576978, "a", lambda: a))
_l_(576980)
_c_(576983, _n_(576981, "print", lambda: print), _n_(576982, "b", lambda: b))
_l_(576984)
_c_(576987, _n_(576985, "print", lambda: print), _n_(576986, "c", lambda: c))
_l_(576988)
_c_(576991, _n_(576989, "print", lambda: print), _n_(576990, "d", lambda: d))
_l_(576992)