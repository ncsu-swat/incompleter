# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(34007)

except ImportError:
    pass
try:
    import os
    _l_(34009)

except ImportError:
    pass
_c_(34011, _n_(34010, "print", lambda: print), 'Select a random element from a list:')
_l_(34012)
elements = [1, 2, 3, 4, 5]
_l_(34013)
_c_(34019, _n_(34014, "print", lambda: print), _c_(34018, _a_(34016, _n_(34015, "random", lambda: random), "choice"), _n_(34017, "elements", lambda: elements)))
_l_(34020)
_c_(34026, _n_(34021, "print", lambda: print), _c_(34025, _a_(34023, _n_(34022, "random", lambda: random), "choice"), _n_(34024, "elements", lambda: elements)))
_l_(34027)
_c_(34033, _n_(34028, "print", lambda: print), _c_(34032, _a_(34030, _n_(34029, "random", lambda: random), "choice"), _n_(34031, "elements", lambda: elements)))
_l_(34034)
_c_(34036, _n_(34035, "print", lambda: print), '\nSelect a random element from a set:')
_l_(34037)
elements = _c_(34039, _n_(34038, "set", lambda: set), [1, 2, 3, 4, 5])
_l_(34040)
_c_(34048, _n_(34041, "print", lambda: print), _c_(34047, _a_(34043, _n_(34042, "random", lambda: random), "choice"), _c_(34046, _n_(34044, "tuple", lambda: tuple), _n_(34045, "elements", lambda: elements))))
_l_(34049)
_c_(34057, _n_(34050, "print", lambda: print), _c_(34056, _a_(34052, _n_(34051, "random", lambda: random), "choice"), _c_(34055, _n_(34053, "tuple", lambda: tuple), _n_(34054, "elements", lambda: elements))))
_l_(34058)
_c_(34066, _n_(34059, "print", lambda: print), _c_(34065, _a_(34061, _n_(34060, "random", lambda: random), "choice"), _c_(34064, _n_(34062, "tuple", lambda: tuple), _n_(34063, "elements", lambda: elements))))
_l_(34067)
_c_(34069, _n_(34068, "print", lambda: print), '\nSelect a random value from a dictionary:')
_l_(34070)
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
_l_(34071)
key = _c_(34077, _a_(34073, _n_(34072, "random", lambda: random), "choice"), _c_(34076, _n_(34074, "list", lambda: list), _n_(34075, "d", lambda: d)))
_l_(34078)
_c_(34082, _n_(34079, "print", lambda: print), _n_(34080, "d", lambda: d)[_n_(34081, "key", lambda: key)])
_l_(34083)
key = _c_(34089, _a_(34085, _n_(34084, "random", lambda: random), "choice"), _c_(34088, _n_(34086, "list", lambda: list), _n_(34087, "d", lambda: d)))
_l_(34090)
_c_(34094, _n_(34091, "print", lambda: print), _n_(34092, "d", lambda: d)[_n_(34093, "key", lambda: key)])
_l_(34095)
_c_(34099, _n_(34096, "print", lambda: print), _n_(34097, "d", lambda: d)[_n_(34098, "key", lambda: key)])
_l_(34100)
_c_(34102, _n_(34101, "print", lambda: print), '\nSelect a random file from a directory.:')
_l_(34103)
_c_(34111, _n_(34104, "print", lambda: print), _c_(34110, _a_(34106, _n_(34105, "random", lambda: random), "choice"), _c_(34109, _a_(34108, _n_(34107, "os", lambda: os), "listdir"), '/')))
_l_(34112)