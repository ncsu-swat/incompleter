# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(117481)

except ImportError:
    pass
_c_(117484, _a_(117483, _n_(117482, "np", lambda: np), "set_printoptions"), linewidth=100)
_l_(117485)
student = _c_(117488, _a_(117487, _n_(117486, "np", lambda: np), "array"), [['01', 'V', 'Debby Pramod'], ['02', 'V', 'Artemiy Ellie'], ['03', 'V', 'Baptist Kamal'], ['04', 'V', 'Lavanya Davide'], ['05', 'V', 'Fulton Antwan'], ['06', 'V', 'Euanthe Sandeep'], ['07', 'V', 'Endzela Sanda'], ['08', 'V', 'Victoire Waman'], ['09', 'V', 'Briar Nur'], ['10', 'V', 'Rose Lykos']])
_l_(117489)
_c_(117491, _n_(117490, "print", lambda: print), 'Original array:')
_l_(117492)
_c_(117495, _n_(117493, "print", lambda: print), _n_(117494, "student", lambda: student))
_l_(117496)
char = 'E'
_l_(117497)
_c_(117500, _n_(117498, "print", lambda: print), '\nStudent name starting with', _n_(117499, "char", lambda: char), ':')
_l_(117501)
_c_(117504, _n_(117502, "print", lambda: print), _n_(117503, "result", lambda: result))
_l_(117505)
char = '1'
_l_(117506)
result = _n_(117507, "student", lambda: student)[_c_(117513, _a_(117510, _a_(117509, _n_(117508, "np", lambda: np), "char"), "startswith"), _n_(117511, "student", lambda: student)[:, 0], _n_(117512, "char", lambda: char))]
_l_(117514)
_c_(117517, _n_(117515, "print", lambda: print), '\nStudent id starting with', _n_(117516, "char", lambda: char), ':')
_l_(117518)
_c_(117521, _n_(117519, "print", lambda: print), _n_(117520, "result", lambda: result))
_l_(117522)