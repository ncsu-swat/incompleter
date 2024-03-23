# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(88087)

except ImportError:
    pass
_c_(88089, _n_(88088, "print", lambda: print), 'Original array:')
_l_(88090)
_c_(88093, _n_(88091, "print", lambda: print), _n_(88092, "nums", lambda: nums))
_l_(88094)
_c_(88096, _n_(88095, "print", lambda: print), '\nSort the said array by row in ascending order:')
_l_(88097)
_c_(88103, _n_(88098, "print", lambda: print), _c_(88102, _a_(88100, _n_(88099, "np", lambda: np), "sort"), _n_(88101, "nums", lambda: nums)))
_l_(88104)
_c_(88106, _n_(88105, "print", lambda: print), '\nSort the said array by column in ascending order:')
_l_(88107)
_c_(88113, _n_(88108, "print", lambda: print), _c_(88112, _a_(88110, _n_(88109, "np", lambda: np), "sort"), _n_(88111, "nums", lambda: nums), axis=0))
_l_(88114)