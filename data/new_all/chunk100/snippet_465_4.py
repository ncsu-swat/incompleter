# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(49307)

except ImportError:
    pass
_c_(49310, _a_(49309, _n_(49308, "np", lambda: np), "set_printoptions"), linewidth=100)
_l_(49311)
_c_(49313, _n_(49312, "print", lambda: print), 'Original array:')
_l_(49314)
_c_(49317, _n_(49315, "print", lambda: print), _n_(49316, "student", lambda: student))
_l_(49318)
char = 'E'
_l_(49319)
result = _n_(49320, "student", lambda: student)[_c_(49326, _a_(49323, _a_(49322, _n_(49321, "np", lambda: np), "char"), "startswith"), _n_(49324, "student", lambda: student)[:, 2], _n_(49325, "char", lambda: char))]
_l_(49327)
_c_(49330, _n_(49328, "print", lambda: print), '\nStudent name starting with', _n_(49329, "char", lambda: char), ':')
_l_(49331)
_c_(49334, _n_(49332, "print", lambda: print), _n_(49333, "result", lambda: result))
_l_(49335)
char = '1'
_l_(49336)
result = _n_(49337, "student", lambda: student)[_c_(49343, _a_(49340, _a_(49339, _n_(49338, "np", lambda: np), "char"), "startswith"), _n_(49341, "student", lambda: student)[:, 0], _n_(49342, "char", lambda: char))]
_l_(49344)
_c_(49347, _n_(49345, "print", lambda: print), '\nStudent id starting with', _n_(49346, "char", lambda: char), ':')
_l_(49348)
_c_(49351, _n_(49349, "print", lambda: print), _n_(49350, "result", lambda: result))
_l_(49352)