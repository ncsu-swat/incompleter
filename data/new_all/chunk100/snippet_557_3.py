# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(57709)

except ImportError:
    pass
try:
    import numpy as np
    _l_(57711)

except ImportError:
    pass
sr1 = _c_(57714, _a_(57713, _n_(57712, "pd", lambda: pd), "Series"), [1, 2, 3, 4, 5])
_l_(57715)
sr2 = _c_(57718, _a_(57717, _n_(57716, "pd", lambda: pd), "Series"), [2, 4, 6, 8, 10])
_l_(57719)
_c_(57721, _n_(57720, "print", lambda: print), 'Original Series:')
_l_(57722)
_c_(57724, _n_(57723, "print", lambda: print), 'sr1:')
_l_(57725)
_c_(57728, _n_(57726, "print", lambda: print), _n_(57727, "sr1", lambda: sr1))
_l_(57729)
_c_(57731, _n_(57730, "print", lambda: print), 'sr2:')
_l_(57732)
_c_(57735, _n_(57733, "print", lambda: print), _n_(57734, "sr2", lambda: sr2))
_l_(57736)
_c_(57738, _n_(57737, "print", lambda: print), '\nItems of a given series not present in another given series:')
_l_(57739)
sr11 = _c_(57747, _a_(57741, _n_(57740, "pd", lambda: pd), "Series"), _c_(57746, _a_(57743, _n_(57742, "np", lambda: np), "union1d"), _n_(57744, "sr1", lambda: sr1), _n_(57745, "sr2", lambda: sr2)))
_l_(57748)
sr22 = _c_(57756, _a_(57750, _n_(57749, "pd", lambda: pd), "Series"), _c_(57755, _a_(57752, _n_(57751, "np", lambda: np), "intersect1d"), _n_(57753, "sr1", lambda: sr1), _n_(57754, "sr2", lambda: sr2)))
_l_(57757)
_c_(57760, _n_(57758, "print", lambda: print), _n_(57759, "result", lambda: result))
_l_(57761)