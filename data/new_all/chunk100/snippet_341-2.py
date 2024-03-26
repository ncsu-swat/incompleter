# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(111249)

except ImportError:
    pass
try:
    import os
    _l_(111251)

except ImportError:
    pass
_c_(111253, _n_(111252, "print", lambda: print), 'Select a random element from a list:')
_l_(111254)
_c_(111260, _n_(111255, "print", lambda: print), _c_(111259, _a_(111257, _n_(111256, "random", lambda: random), "choice"), _n_(111258, "elements", lambda: elements)))
_l_(111261)
_c_(111267, _n_(111262, "print", lambda: print), _c_(111266, _a_(111264, _n_(111263, "random", lambda: random), "choice"), _n_(111265, "elements", lambda: elements)))
_l_(111268)
_c_(111274, _n_(111269, "print", lambda: print), _c_(111273, _a_(111271, _n_(111270, "random", lambda: random), "choice"), _n_(111272, "elements", lambda: elements)))
_l_(111275)
_c_(111277, _n_(111276, "print", lambda: print), '\nSelect a random element from a set:')
_l_(111278)
elements = _c_(111280, _n_(111279, "set", lambda: set), [1, 2, 3, 4, 5])
_l_(111281)
_c_(111289, _n_(111282, "print", lambda: print), _c_(111288, _a_(111284, _n_(111283, "random", lambda: random), "choice"), _c_(111287, _n_(111285, "tuple", lambda: tuple), _n_(111286, "elements", lambda: elements))))
_l_(111290)
_c_(111298, _n_(111291, "print", lambda: print), _c_(111297, _a_(111293, _n_(111292, "random", lambda: random), "choice"), _c_(111296, _n_(111294, "tuple", lambda: tuple), _n_(111295, "elements", lambda: elements))))
_l_(111299)
_c_(111307, _n_(111300, "print", lambda: print), _c_(111306, _a_(111302, _n_(111301, "random", lambda: random), "choice"), _c_(111305, _n_(111303, "tuple", lambda: tuple), _n_(111304, "elements", lambda: elements))))
_l_(111308)
_c_(111310, _n_(111309, "print", lambda: print), '\nSelect a random value from a dictionary:')
_l_(111311)
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
_l_(111312)
key = _c_(111318, _a_(111314, _n_(111313, "random", lambda: random), "choice"), _c_(111317, _n_(111315, "list", lambda: list), _n_(111316, "d", lambda: d)))
_l_(111319)
_c_(111323, _n_(111320, "print", lambda: print), _n_(111321, "d", lambda: d)[_n_(111322, "key", lambda: key)])
_l_(111324)
key = _c_(111330, _a_(111326, _n_(111325, "random", lambda: random), "choice"), _c_(111329, _n_(111327, "list", lambda: list), _n_(111328, "d", lambda: d)))
_l_(111331)
_c_(111335, _n_(111332, "print", lambda: print), _n_(111333, "d", lambda: d)[_n_(111334, "key", lambda: key)])
_l_(111336)
key = _c_(111342, _a_(111338, _n_(111337, "random", lambda: random), "choice"), _c_(111341, _n_(111339, "list", lambda: list), _n_(111340, "d", lambda: d)))
_l_(111343)
_c_(111347, _n_(111344, "print", lambda: print), _n_(111345, "d", lambda: d)[_n_(111346, "key", lambda: key)])
_l_(111348)
_c_(111350, _n_(111349, "print", lambda: print), '\nSelect a random file from a directory.:')
_l_(111351)
_c_(111359, _n_(111352, "print", lambda: print), _c_(111358, _a_(111354, _n_(111353, "random", lambda: random), "choice"), _c_(111357, _a_(111356, _n_(111355, "os", lambda: os), "listdir"), '/')))
_l_(111360)