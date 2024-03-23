# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(49257)

except ImportError:
    pass
_c_(49260, _a_(49259, _n_(49258, "np", lambda: np), "set_printoptions"), linewidth=100)
_l_(49261)
student = _c_(49264, _a_(49263, _n_(49262, "np", lambda: np), "array"), [['01', 'V', 'Debby Pramod'], ['02', 'V', 'Artemiy Ellie'], ['03', 'V', 'Baptist Kamal'], ['04', 'V', 'Lavanya Davide'], ['05', 'V', 'Fulton Antwan'], ['06', 'V', 'Euanthe Sandeep'], ['07', 'V', 'Endzela Sanda'], ['08', 'V', 'Victoire Waman'], ['09', 'V', 'Briar Nur'], ['10', 'V', 'Rose Lykos']])
_l_(49265)
_c_(49267, _n_(49266, "print", lambda: print), 'Original array:')
_l_(49268)
_c_(49271, _n_(49269, "print", lambda: print), _n_(49270, "student", lambda: student))
_l_(49272)
char = 'E'
_l_(49273)
result = _n_(49274, "student", lambda: student)[_c_(49280, _a_(49277, _a_(49276, _n_(49275, "np", lambda: np), "char"), "startswith"), _n_(49278, "student", lambda: student)[:, 2], _n_(49279, "char", lambda: char))]
_l_(49281)
_c_(49284, _n_(49282, "print", lambda: print), '\nStudent name starting with', _n_(49283, "char", lambda: char), ':')
_l_(49285)
_c_(49288, _n_(49286, "print", lambda: print), _n_(49287, "result", lambda: result))
_l_(49289)
result = _n_(49290, "student", lambda: student)[_c_(49296, _a_(49293, _a_(49292, _n_(49291, "np", lambda: np), "char"), "startswith"), _n_(49294, "student", lambda: student)[:, 0], _n_(49295, "char", lambda: char))]
_l_(49297)
_c_(49300, _n_(49298, "print", lambda: print), '\nStudent id starting with', _n_(49299, "char", lambda: char), ':')
_l_(49301)
_c_(49304, _n_(49302, "print", lambda: print), _n_(49303, "result", lambda: result))
_l_(49305)