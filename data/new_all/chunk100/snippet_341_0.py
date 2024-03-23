# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(33569)

except ImportError:
    pass
try:
    import os
    _l_(33571)

except ImportError:
    pass
_c_(33573, _n_(33572, "print", lambda: print), 'Select a random element from a list:')
_l_(33574)
elements = [1, 2, 3, 4, 5]
_l_(33575)
_c_(33581, _n_(33576, "print", lambda: print), _c_(33580, _a_(33578, _n_(33577, "random", lambda: random), "choice"), _n_(33579, "elements", lambda: elements)))
_l_(33582)
_c_(33588, _n_(33583, "print", lambda: print), _c_(33587, _a_(33585, _n_(33584, "random", lambda: random), "choice"), _n_(33586, "elements", lambda: elements)))
_l_(33589)
_c_(33595, _n_(33590, "print", lambda: print), _c_(33594, _a_(33592, _n_(33591, "random", lambda: random), "choice"), _n_(33593, "elements", lambda: elements)))
_l_(33596)
_c_(33598, _n_(33597, "print", lambda: print), '\nSelect a random element from a set:')
_l_(33599)
elements = _c_(33601, _n_(33600, "set", lambda: set), [1, 2, 3, 4, 5])
_l_(33602)
_c_(33610, _n_(33603, "print", lambda: print), _c_(33609, _a_(33605, _n_(33604, "random", lambda: random), "choice"), _c_(33608, _n_(33606, "tuple", lambda: tuple), _n_(33607, "elements", lambda: elements))))
_l_(33611)
_c_(33619, _n_(33612, "print", lambda: print), _c_(33618, _a_(33614, _n_(33613, "random", lambda: random), "choice"), _c_(33617, _n_(33615, "tuple", lambda: tuple), _n_(33616, "elements", lambda: elements))))
_l_(33620)
_c_(33628, _n_(33621, "print", lambda: print), _c_(33627, _a_(33623, _n_(33622, "random", lambda: random), "choice"), _c_(33626, _n_(33624, "tuple", lambda: tuple), _n_(33625, "elements", lambda: elements))))
_l_(33629)
_c_(33631, _n_(33630, "print", lambda: print), '\nSelect a random value from a dictionary:')
_l_(33632)
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
_l_(33633)
key = _c_(33639, _a_(33635, _n_(33634, "random", lambda: random), "choice"), _c_(33638, _n_(33636, "list", lambda: list), _n_(33637, "d", lambda: d)))
_l_(33640)
_c_(33644, _n_(33641, "print", lambda: print), _n_(33642, "d", lambda: d)[_n_(33643, "key", lambda: key)])
_l_(33645)
_c_(33649, _n_(33646, "print", lambda: print), _n_(33647, "d", lambda: d)[_n_(33648, "key", lambda: key)])
_l_(33650)
key = _c_(33656, _a_(33652, _n_(33651, "random", lambda: random), "choice"), _c_(33655, _n_(33653, "list", lambda: list), _n_(33654, "d", lambda: d)))
_l_(33657)
_c_(33661, _n_(33658, "print", lambda: print), _n_(33659, "d", lambda: d)[_n_(33660, "key", lambda: key)])
_l_(33662)
_c_(33664, _n_(33663, "print", lambda: print), '\nSelect a random file from a directory.:')
_l_(33665)
_c_(33673, _n_(33666, "print", lambda: print), _c_(33672, _a_(33668, _n_(33667, "random", lambda: random), "choice"), _c_(33671, _a_(33670, _n_(33669, "os", lambda: os), "listdir"), '/')))
_l_(33674)