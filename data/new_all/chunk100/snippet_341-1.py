# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(111142)

except ImportError:
    pass
try:
    import os
    _l_(111144)

except ImportError:
    pass
_c_(111146, _n_(111145, "print", lambda: print), 'Select a random element from a list:')
_l_(111147)
elements = [1, 2, 3, 4, 5]
_l_(111148)
_c_(111154, _n_(111149, "print", lambda: print), _c_(111153, _a_(111151, _n_(111150, "random", lambda: random), "choice"), _n_(111152, "elements", lambda: elements)))
_l_(111155)
_c_(111161, _n_(111156, "print", lambda: print), _c_(111160, _a_(111158, _n_(111157, "random", lambda: random), "choice"), _n_(111159, "elements", lambda: elements)))
_l_(111162)
_c_(111168, _n_(111163, "print", lambda: print), _c_(111167, _a_(111165, _n_(111164, "random", lambda: random), "choice"), _n_(111166, "elements", lambda: elements)))
_l_(111169)
_c_(111171, _n_(111170, "print", lambda: print), '\nSelect a random element from a set:')
_l_(111172)
elements = _c_(111174, _n_(111173, "set", lambda: set), [1, 2, 3, 4, 5])
_l_(111175)
_c_(111183, _n_(111176, "print", lambda: print), _c_(111182, _a_(111178, _n_(111177, "random", lambda: random), "choice"), _c_(111181, _n_(111179, "tuple", lambda: tuple), _n_(111180, "elements", lambda: elements))))
_l_(111184)
_c_(111192, _n_(111185, "print", lambda: print), _c_(111191, _a_(111187, _n_(111186, "random", lambda: random), "choice"), _c_(111190, _n_(111188, "tuple", lambda: tuple), _n_(111189, "elements", lambda: elements))))
_l_(111193)
_c_(111201, _n_(111194, "print", lambda: print), _c_(111200, _a_(111196, _n_(111195, "random", lambda: random), "choice"), _c_(111199, _n_(111197, "tuple", lambda: tuple), _n_(111198, "elements", lambda: elements))))
_l_(111202)
_c_(111204, _n_(111203, "print", lambda: print), '\nSelect a random value from a dictionary:')
_l_(111205)
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
_l_(111206)
_c_(111210, _n_(111207, "print", lambda: print), _n_(111208, "d", lambda: d)[_n_(111209, "key", lambda: key)])
_l_(111211)
key = _c_(111217, _a_(111213, _n_(111212, "random", lambda: random), "choice"), _c_(111216, _n_(111214, "list", lambda: list), _n_(111215, "d", lambda: d)))
_l_(111218)
_c_(111222, _n_(111219, "print", lambda: print), _n_(111220, "d", lambda: d)[_n_(111221, "key", lambda: key)])
_l_(111223)
key = _c_(111229, _a_(111225, _n_(111224, "random", lambda: random), "choice"), _c_(111228, _n_(111226, "list", lambda: list), _n_(111227, "d", lambda: d)))
_l_(111230)
_c_(111234, _n_(111231, "print", lambda: print), _n_(111232, "d", lambda: d)[_n_(111233, "key", lambda: key)])
_l_(111235)
_c_(111237, _n_(111236, "print", lambda: print), '\nSelect a random file from a directory.:')
_l_(111238)
_c_(111246, _n_(111239, "print", lambda: print), _c_(111245, _a_(111241, _n_(111240, "random", lambda: random), "choice"), _c_(111244, _a_(111243, _n_(111242, "os", lambda: os), "listdir"), '/')))
_l_(111247)