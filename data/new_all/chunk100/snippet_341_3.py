# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(33900)

except ImportError:
    pass
try:
    import os
    _l_(33902)

except ImportError:
    pass
_c_(33904, _n_(33903, "print", lambda: print), 'Select a random element from a list:')
_l_(33905)
elements = [1, 2, 3, 4, 5]
_l_(33906)
_c_(33912, _n_(33907, "print", lambda: print), _c_(33911, _a_(33909, _n_(33908, "random", lambda: random), "choice"), _n_(33910, "elements", lambda: elements)))
_l_(33913)
_c_(33919, _n_(33914, "print", lambda: print), _c_(33918, _a_(33916, _n_(33915, "random", lambda: random), "choice"), _n_(33917, "elements", lambda: elements)))
_l_(33920)
_c_(33926, _n_(33921, "print", lambda: print), _c_(33925, _a_(33923, _n_(33922, "random", lambda: random), "choice"), _n_(33924, "elements", lambda: elements)))
_l_(33927)
_c_(33929, _n_(33928, "print", lambda: print), '\nSelect a random element from a set:')
_l_(33930)
elements = _c_(33932, _n_(33931, "set", lambda: set), [1, 2, 3, 4, 5])
_l_(33933)
_c_(33941, _n_(33934, "print", lambda: print), _c_(33940, _a_(33936, _n_(33935, "random", lambda: random), "choice"), _c_(33939, _n_(33937, "tuple", lambda: tuple), _n_(33938, "elements", lambda: elements))))
_l_(33942)
_c_(33950, _n_(33943, "print", lambda: print), _c_(33949, _a_(33945, _n_(33944, "random", lambda: random), "choice"), _c_(33948, _n_(33946, "tuple", lambda: tuple), _n_(33947, "elements", lambda: elements))))
_l_(33951)
_c_(33959, _n_(33952, "print", lambda: print), _c_(33958, _a_(33954, _n_(33953, "random", lambda: random), "choice"), _c_(33957, _n_(33955, "tuple", lambda: tuple), _n_(33956, "elements", lambda: elements))))
_l_(33960)
_c_(33962, _n_(33961, "print", lambda: print), '\nSelect a random value from a dictionary:')
_l_(33963)
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
_l_(33964)
_c_(33968, _n_(33965, "print", lambda: print), _n_(33966, "d", lambda: d)[_n_(33967, "key", lambda: key)])
_l_(33969)
key = _c_(33975, _a_(33971, _n_(33970, "random", lambda: random), "choice"), _c_(33974, _n_(33972, "list", lambda: list), _n_(33973, "d", lambda: d)))
_l_(33976)
_c_(33980, _n_(33977, "print", lambda: print), _n_(33978, "d", lambda: d)[_n_(33979, "key", lambda: key)])
_l_(33981)
key = _c_(33987, _a_(33983, _n_(33982, "random", lambda: random), "choice"), _c_(33986, _n_(33984, "list", lambda: list), _n_(33985, "d", lambda: d)))
_l_(33988)
_c_(33992, _n_(33989, "print", lambda: print), _n_(33990, "d", lambda: d)[_n_(33991, "key", lambda: key)])
_l_(33993)
_c_(33995, _n_(33994, "print", lambda: print), '\nSelect a random file from a directory.:')
_l_(33996)
_c_(34004, _n_(33997, "print", lambda: print), _c_(34003, _a_(33999, _n_(33998, "random", lambda: random), "choice"), _c_(34002, _a_(34001, _n_(34000, "os", lambda: os), "listdir"), '/')))
_l_(34005)