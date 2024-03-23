# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(57602)

except ImportError:
    pass
try:
    import numpy as np
    _l_(57604)

except ImportError:
    pass
sr1 = _c_(57607, _a_(57606, _n_(57605, "pd", lambda: pd), "Series"), [1, 2, 3, 4, 5])
_l_(57608)
_c_(57610, _n_(57609, "print", lambda: print), 'Original Series:')
_l_(57611)
_c_(57613, _n_(57612, "print", lambda: print), 'sr1:')
_l_(57614)
_c_(57617, _n_(57615, "print", lambda: print), _n_(57616, "sr1", lambda: sr1))
_l_(57618)
_c_(57620, _n_(57619, "print", lambda: print), 'sr2:')
_l_(57621)
_c_(57624, _n_(57622, "print", lambda: print), _n_(57623, "sr2", lambda: sr2))
_l_(57625)
_c_(57627, _n_(57626, "print", lambda: print), '\nItems of a given series not present in another given series:')
_l_(57628)
sr11 = _c_(57636, _a_(57630, _n_(57629, "pd", lambda: pd), "Series"), _c_(57635, _a_(57632, _n_(57631, "np", lambda: np), "union1d"), _n_(57633, "sr1", lambda: sr1), _n_(57634, "sr2", lambda: sr2)))
_l_(57637)
sr22 = _c_(57645, _a_(57639, _n_(57638, "pd", lambda: pd), "Series"), _c_(57644, _a_(57641, _n_(57640, "np", lambda: np), "intersect1d"), _n_(57642, "sr1", lambda: sr1), _n_(57643, "sr2", lambda: sr2)))
_l_(57646)
result = _n_(57647, "sr11", lambda: sr11)[~_c_(57651, _a_(57649, _n_(57648, "sr11", lambda: sr11), "isin"), _n_(57650, "sr22", lambda: sr22))]
_l_(57652)
_c_(57655, _n_(57653, "print", lambda: print), _n_(57654, "result", lambda: result))
_l_(57656)