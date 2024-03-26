# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(111029)

except ImportError:
    pass
try:
    import os
    _l_(111031)

except ImportError:
    pass
_c_(111033, _n_(111032, "print", lambda: print), 'Select a random element from a list:')
_l_(111034)
elements = [1, 2, 3, 4, 5]
_l_(111035)
_c_(111041, _n_(111036, "print", lambda: print), _c_(111040, _a_(111038, _n_(111037, "random", lambda: random), "choice"), _n_(111039, "elements", lambda: elements)))
_l_(111042)
_c_(111048, _n_(111043, "print", lambda: print), _c_(111047, _a_(111045, _n_(111044, "random", lambda: random), "choice"), _n_(111046, "elements", lambda: elements)))
_l_(111049)
_c_(111055, _n_(111050, "print", lambda: print), _c_(111054, _a_(111052, _n_(111051, "random", lambda: random), "choice"), _n_(111053, "elements", lambda: elements)))
_l_(111056)
_c_(111058, _n_(111057, "print", lambda: print), '\nSelect a random element from a set:')
_l_(111059)
elements = _c_(111061, _n_(111060, "set", lambda: set), [1, 2, 3, 4, 5])
_l_(111062)
_c_(111070, _n_(111063, "print", lambda: print), _c_(111069, _a_(111065, _n_(111064, "random", lambda: random), "choice"), _c_(111068, _n_(111066, "tuple", lambda: tuple), _n_(111067, "elements", lambda: elements))))
_l_(111071)
_c_(111079, _n_(111072, "print", lambda: print), _c_(111078, _a_(111074, _n_(111073, "random", lambda: random), "choice"), _c_(111077, _n_(111075, "tuple", lambda: tuple), _n_(111076, "elements", lambda: elements))))
_l_(111080)
_c_(111088, _n_(111081, "print", lambda: print), _c_(111087, _a_(111083, _n_(111082, "random", lambda: random), "choice"), _c_(111086, _n_(111084, "tuple", lambda: tuple), _n_(111085, "elements", lambda: elements))))
_l_(111089)
_c_(111091, _n_(111090, "print", lambda: print), '\nSelect a random value from a dictionary:')
_l_(111092)
key = _c_(111098, _a_(111094, _n_(111093, "random", lambda: random), "choice"), _c_(111097, _n_(111095, "list", lambda: list), _n_(111096, "d", lambda: d)))
_l_(111099)
_c_(111103, _n_(111100, "print", lambda: print), _n_(111101, "d", lambda: d)[_n_(111102, "key", lambda: key)])
_l_(111104)
key = _c_(111110, _a_(111106, _n_(111105, "random", lambda: random), "choice"), _c_(111109, _n_(111107, "list", lambda: list), _n_(111108, "d", lambda: d)))
_l_(111111)
_c_(111115, _n_(111112, "print", lambda: print), _n_(111113, "d", lambda: d)[_n_(111114, "key", lambda: key)])
_l_(111116)
key = _c_(111122, _a_(111118, _n_(111117, "random", lambda: random), "choice"), _c_(111121, _n_(111119, "list", lambda: list), _n_(111120, "d", lambda: d)))
_l_(111123)
_c_(111127, _n_(111124, "print", lambda: print), _n_(111125, "d", lambda: d)[_n_(111126, "key", lambda: key)])
_l_(111128)
_c_(111130, _n_(111129, "print", lambda: print), '\nSelect a random file from a directory.:')
_l_(111131)
_c_(111139, _n_(111132, "print", lambda: print), _c_(111138, _a_(111134, _n_(111133, "random", lambda: random), "choice"), _c_(111137, _a_(111136, _n_(111135, "os", lambda: os), "listdir"), '/')))
_l_(111140)