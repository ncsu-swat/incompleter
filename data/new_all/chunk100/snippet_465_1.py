# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(49171)

except ImportError:
    pass
_c_(49174, _a_(49173, _n_(49172, "np", lambda: np), "set_printoptions"), linewidth=100)
_l_(49175)
student = _c_(49178, _a_(49177, _n_(49176, "np", lambda: np), "array"), [['01', 'V', 'Debby Pramod'], ['02', 'V', 'Artemiy Ellie'], ['03', 'V', 'Baptist Kamal'], ['04', 'V', 'Lavanya Davide'], ['05', 'V', 'Fulton Antwan'], ['06', 'V', 'Euanthe Sandeep'], ['07', 'V', 'Endzela Sanda'], ['08', 'V', 'Victoire Waman'], ['09', 'V', 'Briar Nur'], ['10', 'V', 'Rose Lykos']])
_l_(49179)
_c_(49181, _n_(49180, "print", lambda: print), 'Original array:')
_l_(49182)
_c_(49185, _n_(49183, "print", lambda: print), _n_(49184, "student", lambda: student))
_l_(49186)
char = 'E'
_l_(49187)
_c_(49190, _n_(49188, "print", lambda: print), '\nStudent name starting with', _n_(49189, "char", lambda: char), ':')
_l_(49191)
_c_(49194, _n_(49192, "print", lambda: print), _n_(49193, "result", lambda: result))
_l_(49195)
char = '1'
_l_(49196)
result = _n_(49197, "student", lambda: student)[_c_(49203, _a_(49200, _a_(49199, _n_(49198, "np", lambda: np), "char"), "startswith"), _n_(49201, "student", lambda: student)[:, 0], _n_(49202, "char", lambda: char))]
_l_(49204)
_c_(49207, _n_(49205, "print", lambda: print), '\nStudent id starting with', _n_(49206, "char", lambda: char), ':')
_l_(49208)
_c_(49211, _n_(49209, "print", lambda: print), _n_(49210, "result", lambda: result))
_l_(49212)