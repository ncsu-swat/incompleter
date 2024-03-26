# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(117431)

except ImportError:
    pass
_c_(117434, _a_(117433, _n_(117432, "np", lambda: np), "set_printoptions"), linewidth=100)
_l_(117435)
student = _c_(117438, _a_(117437, _n_(117436, "np", lambda: np), "array"), [['01', 'V', 'Debby Pramod'], ['02', 'V', 'Artemiy Ellie'], ['03', 'V', 'Baptist Kamal'], ['04', 'V', 'Lavanya Davide'], ['05', 'V', 'Fulton Antwan'], ['06', 'V', 'Euanthe Sandeep'], ['07', 'V', 'Endzela Sanda'], ['08', 'V', 'Victoire Waman'], ['09', 'V', 'Briar Nur'], ['10', 'V', 'Rose Lykos']])
_l_(117439)
_c_(117441, _n_(117440, "print", lambda: print), 'Original array:')
_l_(117442)
_c_(117445, _n_(117443, "print", lambda: print), _n_(117444, "student", lambda: student))
_l_(117446)
result = _n_(117447, "student", lambda: student)[_c_(117453, _a_(117450, _a_(117449, _n_(117448, "np", lambda: np), "char"), "startswith"), _n_(117451, "student", lambda: student)[:, 2], _n_(117452, "char", lambda: char))]
_l_(117454)
_c_(117457, _n_(117455, "print", lambda: print), '\nStudent name starting with', _n_(117456, "char", lambda: char), ':')
_l_(117458)
_c_(117461, _n_(117459, "print", lambda: print), _n_(117460, "result", lambda: result))
_l_(117462)
char = '1'
_l_(117463)
result = _n_(117464, "student", lambda: student)[_c_(117470, _a_(117467, _a_(117466, _n_(117465, "np", lambda: np), "char"), "startswith"), _n_(117468, "student", lambda: student)[:, 0], _n_(117469, "char", lambda: char))]
_l_(117471)
_c_(117474, _n_(117472, "print", lambda: print), '\nStudent id starting with', _n_(117473, "char", lambda: char), ':')
_l_(117475)
_c_(117478, _n_(117476, "print", lambda: print), _n_(117477, "result", lambda: result))
_l_(117479)