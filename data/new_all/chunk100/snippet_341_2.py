# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(33789)

except ImportError:
    pass
try:
    import os
    _l_(33791)

except ImportError:
    pass
_c_(33793, _n_(33792, "print", lambda: print), 'Select a random element from a list:')
_l_(33794)
elements = [1, 2, 3, 4, 5]
_l_(33795)
_c_(33801, _n_(33796, "print", lambda: print), _c_(33800, _a_(33798, _n_(33797, "random", lambda: random), "choice"), _n_(33799, "elements", lambda: elements)))
_l_(33802)
_c_(33808, _n_(33803, "print", lambda: print), _c_(33807, _a_(33805, _n_(33804, "random", lambda: random), "choice"), _n_(33806, "elements", lambda: elements)))
_l_(33809)
_c_(33815, _n_(33810, "print", lambda: print), _c_(33814, _a_(33812, _n_(33811, "random", lambda: random), "choice"), _n_(33813, "elements", lambda: elements)))
_l_(33816)
_c_(33818, _n_(33817, "print", lambda: print), '\nSelect a random element from a set:')
_l_(33819)
_c_(33827, _n_(33820, "print", lambda: print), _c_(33826, _a_(33822, _n_(33821, "random", lambda: random), "choice"), _c_(33825, _n_(33823, "tuple", lambda: tuple), _n_(33824, "elements", lambda: elements))))
_l_(33828)
_c_(33836, _n_(33829, "print", lambda: print), _c_(33835, _a_(33831, _n_(33830, "random", lambda: random), "choice"), _c_(33834, _n_(33832, "tuple", lambda: tuple), _n_(33833, "elements", lambda: elements))))
_l_(33837)
_c_(33845, _n_(33838, "print", lambda: print), _c_(33844, _a_(33840, _n_(33839, "random", lambda: random), "choice"), _c_(33843, _n_(33841, "tuple", lambda: tuple), _n_(33842, "elements", lambda: elements))))
_l_(33846)
_c_(33848, _n_(33847, "print", lambda: print), '\nSelect a random value from a dictionary:')
_l_(33849)
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
_l_(33850)
key = _c_(33856, _a_(33852, _n_(33851, "random", lambda: random), "choice"), _c_(33855, _n_(33853, "list", lambda: list), _n_(33854, "d", lambda: d)))
_l_(33857)
_c_(33861, _n_(33858, "print", lambda: print), _n_(33859, "d", lambda: d)[_n_(33860, "key", lambda: key)])
_l_(33862)
key = _c_(33868, _a_(33864, _n_(33863, "random", lambda: random), "choice"), _c_(33867, _n_(33865, "list", lambda: list), _n_(33866, "d", lambda: d)))
_l_(33869)
_c_(33873, _n_(33870, "print", lambda: print), _n_(33871, "d", lambda: d)[_n_(33872, "key", lambda: key)])
_l_(33874)
key = _c_(33880, _a_(33876, _n_(33875, "random", lambda: random), "choice"), _c_(33879, _n_(33877, "list", lambda: list), _n_(33878, "d", lambda: d)))
_l_(33881)
_c_(33885, _n_(33882, "print", lambda: print), _n_(33883, "d", lambda: d)[_n_(33884, "key", lambda: key)])
_l_(33886)
_c_(33888, _n_(33887, "print", lambda: print), '\nSelect a random file from a directory.:')
_l_(33889)
_c_(33897, _n_(33890, "print", lambda: print), _c_(33896, _a_(33892, _n_(33891, "random", lambda: random), "choice"), _c_(33895, _a_(33894, _n_(33893, "os", lambda: os), "listdir"), '/')))
_l_(33898)