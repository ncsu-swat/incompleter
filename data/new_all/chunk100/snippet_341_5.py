# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(34114)

except ImportError:
    pass
try:
    import os
    _l_(34116)

except ImportError:
    pass
_c_(34118, _n_(34117, "print", lambda: print), 'Select a random element from a list:')
_l_(34119)
_c_(34125, _n_(34120, "print", lambda: print), _c_(34124, _a_(34122, _n_(34121, "random", lambda: random), "choice"), _n_(34123, "elements", lambda: elements)))
_l_(34126)
_c_(34132, _n_(34127, "print", lambda: print), _c_(34131, _a_(34129, _n_(34128, "random", lambda: random), "choice"), _n_(34130, "elements", lambda: elements)))
_l_(34133)
_c_(34139, _n_(34134, "print", lambda: print), _c_(34138, _a_(34136, _n_(34135, "random", lambda: random), "choice"), _n_(34137, "elements", lambda: elements)))
_l_(34140)
_c_(34142, _n_(34141, "print", lambda: print), '\nSelect a random element from a set:')
_l_(34143)
elements = _c_(34145, _n_(34144, "set", lambda: set), [1, 2, 3, 4, 5])
_l_(34146)
_c_(34154, _n_(34147, "print", lambda: print), _c_(34153, _a_(34149, _n_(34148, "random", lambda: random), "choice"), _c_(34152, _n_(34150, "tuple", lambda: tuple), _n_(34151, "elements", lambda: elements))))
_l_(34155)
_c_(34163, _n_(34156, "print", lambda: print), _c_(34162, _a_(34158, _n_(34157, "random", lambda: random), "choice"), _c_(34161, _n_(34159, "tuple", lambda: tuple), _n_(34160, "elements", lambda: elements))))
_l_(34164)
_c_(34172, _n_(34165, "print", lambda: print), _c_(34171, _a_(34167, _n_(34166, "random", lambda: random), "choice"), _c_(34170, _n_(34168, "tuple", lambda: tuple), _n_(34169, "elements", lambda: elements))))
_l_(34173)
_c_(34175, _n_(34174, "print", lambda: print), '\nSelect a random value from a dictionary:')
_l_(34176)
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
_l_(34177)
key = _c_(34183, _a_(34179, _n_(34178, "random", lambda: random), "choice"), _c_(34182, _n_(34180, "list", lambda: list), _n_(34181, "d", lambda: d)))
_l_(34184)
_c_(34188, _n_(34185, "print", lambda: print), _n_(34186, "d", lambda: d)[_n_(34187, "key", lambda: key)])
_l_(34189)
key = _c_(34195, _a_(34191, _n_(34190, "random", lambda: random), "choice"), _c_(34194, _n_(34192, "list", lambda: list), _n_(34193, "d", lambda: d)))
_l_(34196)
_c_(34200, _n_(34197, "print", lambda: print), _n_(34198, "d", lambda: d)[_n_(34199, "key", lambda: key)])
_l_(34201)
key = _c_(34207, _a_(34203, _n_(34202, "random", lambda: random), "choice"), _c_(34206, _n_(34204, "list", lambda: list), _n_(34205, "d", lambda: d)))
_l_(34208)
_c_(34212, _n_(34209, "print", lambda: print), _n_(34210, "d", lambda: d)[_n_(34211, "key", lambda: key)])
_l_(34213)
_c_(34215, _n_(34214, "print", lambda: print), '\nSelect a random file from a directory.:')
_l_(34216)
_c_(34224, _n_(34217, "print", lambda: print), _c_(34223, _a_(34219, _n_(34218, "random", lambda: random), "choice"), _c_(34222, _a_(34221, _n_(34220, "os", lambda: os), "listdir"), '/')))
_l_(34225)