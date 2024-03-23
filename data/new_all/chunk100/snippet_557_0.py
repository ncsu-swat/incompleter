# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(57551)

except ImportError:
    pass
try:
    import numpy as np
    _l_(57553)

except ImportError:
    pass
sr1 = _c_(57556, _a_(57555, _n_(57554, "pd", lambda: pd), "Series"), [1, 2, 3, 4, 5])
_l_(57557)
sr2 = _c_(57560, _a_(57559, _n_(57558, "pd", lambda: pd), "Series"), [2, 4, 6, 8, 10])
_l_(57561)
_c_(57563, _n_(57562, "print", lambda: print), 'Original Series:')
_l_(57564)
_c_(57566, _n_(57565, "print", lambda: print), 'sr1:')
_l_(57567)
_c_(57570, _n_(57568, "print", lambda: print), _n_(57569, "sr1", lambda: sr1))
_l_(57571)
_c_(57573, _n_(57572, "print", lambda: print), 'sr2:')
_l_(57574)
_c_(57577, _n_(57575, "print", lambda: print), _n_(57576, "sr2", lambda: sr2))
_l_(57578)
_c_(57580, _n_(57579, "print", lambda: print), '\nItems of a given series not present in another given series:')
_l_(57581)
sr11 = _c_(57589, _a_(57583, _n_(57582, "pd", lambda: pd), "Series"), _c_(57588, _a_(57585, _n_(57584, "np", lambda: np), "union1d"), _n_(57586, "sr1", lambda: sr1), _n_(57587, "sr2", lambda: sr2)))
_l_(57590)
result = _n_(57591, "sr11", lambda: sr11)[~_c_(57595, _a_(57593, _n_(57592, "sr11", lambda: sr11), "isin"), _n_(57594, "sr22", lambda: sr22))]
_l_(57596)
_c_(57599, _n_(57597, "print", lambda: print), _n_(57598, "result", lambda: result))
_l_(57600)