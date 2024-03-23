# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(49121)

except ImportError:
    pass
_c_(49124, _a_(49123, _n_(49122, "np", lambda: np), "set_printoptions"), linewidth=100)
_l_(49125)
student = _c_(49128, _a_(49127, _n_(49126, "np", lambda: np), "array"), [['01', 'V', 'Debby Pramod'], ['02', 'V', 'Artemiy Ellie'], ['03', 'V', 'Baptist Kamal'], ['04', 'V', 'Lavanya Davide'], ['05', 'V', 'Fulton Antwan'], ['06', 'V', 'Euanthe Sandeep'], ['07', 'V', 'Endzela Sanda'], ['08', 'V', 'Victoire Waman'], ['09', 'V', 'Briar Nur'], ['10', 'V', 'Rose Lykos']])
_l_(49129)
_c_(49131, _n_(49130, "print", lambda: print), 'Original array:')
_l_(49132)
_c_(49135, _n_(49133, "print", lambda: print), _n_(49134, "student", lambda: student))
_l_(49136)
result = _n_(49137, "student", lambda: student)[_c_(49143, _a_(49140, _a_(49139, _n_(49138, "np", lambda: np), "char"), "startswith"), _n_(49141, "student", lambda: student)[:, 2], _n_(49142, "char", lambda: char))]
_l_(49144)
_c_(49147, _n_(49145, "print", lambda: print), '\nStudent name starting with', _n_(49146, "char", lambda: char), ':')
_l_(49148)
_c_(49151, _n_(49149, "print", lambda: print), _n_(49150, "result", lambda: result))
_l_(49152)
char = '1'
_l_(49153)
result = _n_(49154, "student", lambda: student)[_c_(49160, _a_(49157, _a_(49156, _n_(49155, "np", lambda: np), "char"), "startswith"), _n_(49158, "student", lambda: student)[:, 0], _n_(49159, "char", lambda: char))]
_l_(49161)
_c_(49164, _n_(49162, "print", lambda: print), '\nStudent id starting with', _n_(49163, "char", lambda: char), ':')
_l_(49165)
_c_(49168, _n_(49166, "print", lambda: print), _n_(49167, "result", lambda: result))
_l_(49169)