# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from itertools import groupby
    _l_(66209)

except ImportError:
    pass

def compress(l_nums):
    _l_(66215)

    aux = [_n_(66210, "key", lambda: key) for (key, group) in _c_(66213, _n_(66211, "groupby", lambda: groupby), _n_(66212, "l_nums", lambda: l_nums))]
    _l_(66214)
    return aux
_c_(66217, _n_(66216, "print", lambda: print), 'Original list:')
_l_(66218)
_c_(66221, _n_(66219, "print", lambda: print), _n_(66220, "n_list", lambda: n_list))
_l_(66222)
_c_(66224, _n_(66223, "print", lambda: print), '\nAfter removing consecutive duplicates:')
_l_(66225)
_c_(66230, _n_(66226, "print", lambda: print), _c_(66229, _n_(66227, "compress", lambda: compress), _n_(66228, "n_list", lambda: n_list)))
_l_(66231)