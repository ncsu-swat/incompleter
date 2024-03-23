# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(49214)

except ImportError:
    pass
_c_(49217, _a_(49216, _n_(49215, "np", lambda: np), "set_printoptions"), linewidth=100)
_l_(49218)
student = _c_(49221, _a_(49220, _n_(49219, "np", lambda: np), "array"), [['01', 'V', 'Debby Pramod'], ['02', 'V', 'Artemiy Ellie'], ['03', 'V', 'Baptist Kamal'], ['04', 'V', 'Lavanya Davide'], ['05', 'V', 'Fulton Antwan'], ['06', 'V', 'Euanthe Sandeep'], ['07', 'V', 'Endzela Sanda'], ['08', 'V', 'Victoire Waman'], ['09', 'V', 'Briar Nur'], ['10', 'V', 'Rose Lykos']])
_l_(49222)
_c_(49224, _n_(49223, "print", lambda: print), 'Original array:')
_l_(49225)
_c_(49228, _n_(49226, "print", lambda: print), _n_(49227, "student", lambda: student))
_l_(49229)
char = 'E'
_l_(49230)
result = _n_(49231, "student", lambda: student)[_c_(49237, _a_(49234, _a_(49233, _n_(49232, "np", lambda: np), "char"), "startswith"), _n_(49235, "student", lambda: student)[:, 2], _n_(49236, "char", lambda: char))]
_l_(49238)
_c_(49241, _n_(49239, "print", lambda: print), '\nStudent name starting with', _n_(49240, "char", lambda: char), ':')
_l_(49242)
_c_(49245, _n_(49243, "print", lambda: print), _n_(49244, "result", lambda: result))
_l_(49246)
char = '1'
_l_(49247)
_c_(49250, _n_(49248, "print", lambda: print), '\nStudent id starting with', _n_(49249, "char", lambda: char), ':')
_l_(49251)
_c_(49254, _n_(49252, "print", lambda: print), _n_(49253, "result", lambda: result))
_l_(49255)