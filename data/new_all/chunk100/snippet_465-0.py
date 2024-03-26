# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(117384)

except ImportError:
    pass
_c_(117387, _a_(117386, _n_(117385, "np", lambda: np), "set_printoptions"), linewidth=100)
_l_(117388)
_c_(117390, _n_(117389, "print", lambda: print), 'Original array:')
_l_(117391)
_c_(117394, _n_(117392, "print", lambda: print), _n_(117393, "student", lambda: student))
_l_(117395)
char = 'E'
_l_(117396)
result = _n_(117397, "student", lambda: student)[_c_(117403, _a_(117400, _a_(117399, _n_(117398, "np", lambda: np), "char"), "startswith"), _n_(117401, "student", lambda: student)[:, 2], _n_(117402, "char", lambda: char))]
_l_(117404)
_c_(117407, _n_(117405, "print", lambda: print), '\nStudent name starting with', _n_(117406, "char", lambda: char), ':')
_l_(117408)
_c_(117411, _n_(117409, "print", lambda: print), _n_(117410, "result", lambda: result))
_l_(117412)
char = '1'
_l_(117413)
result = _n_(117414, "student", lambda: student)[_c_(117420, _a_(117417, _a_(117416, _n_(117415, "np", lambda: np), "char"), "startswith"), _n_(117418, "student", lambda: student)[:, 0], _n_(117419, "char", lambda: char))]
_l_(117421)
_c_(117424, _n_(117422, "print", lambda: print), '\nStudent id starting with', _n_(117423, "char", lambda: char), ':')
_l_(117425)
_c_(117428, _n_(117426, "print", lambda: print), _n_(117427, "result", lambda: result))
_l_(117429)