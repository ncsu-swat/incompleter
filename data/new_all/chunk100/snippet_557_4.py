# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(57763)

except ImportError:
    pass
try:
    import numpy as np
    _l_(57765)

except ImportError:
    pass
sr2 = _c_(57768, _a_(57767, _n_(57766, "pd", lambda: pd), "Series"), [2, 4, 6, 8, 10])
_l_(57769)
_c_(57771, _n_(57770, "print", lambda: print), 'Original Series:')
_l_(57772)
_c_(57774, _n_(57773, "print", lambda: print), 'sr1:')
_l_(57775)
_c_(57778, _n_(57776, "print", lambda: print), _n_(57777, "sr1", lambda: sr1))
_l_(57779)
_c_(57781, _n_(57780, "print", lambda: print), 'sr2:')
_l_(57782)
_c_(57785, _n_(57783, "print", lambda: print), _n_(57784, "sr2", lambda: sr2))
_l_(57786)
_c_(57788, _n_(57787, "print", lambda: print), '\nItems of a given series not present in another given series:')
_l_(57789)
sr11 = _c_(57797, _a_(57791, _n_(57790, "pd", lambda: pd), "Series"), _c_(57796, _a_(57793, _n_(57792, "np", lambda: np), "union1d"), _n_(57794, "sr1", lambda: sr1), _n_(57795, "sr2", lambda: sr2)))
_l_(57798)
sr22 = _c_(57806, _a_(57800, _n_(57799, "pd", lambda: pd), "Series"), _c_(57805, _a_(57802, _n_(57801, "np", lambda: np), "intersect1d"), _n_(57803, "sr1", lambda: sr1), _n_(57804, "sr2", lambda: sr2)))
_l_(57807)
result = _n_(57808, "sr11", lambda: sr11)[~_c_(57812, _a_(57810, _n_(57809, "sr11", lambda: sr11), "isin"), _n_(57811, "sr22", lambda: sr22))]
_l_(57813)
_c_(57816, _n_(57814, "print", lambda: print), _n_(57815, "result", lambda: result))
_l_(57817)