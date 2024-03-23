# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(57658)

except ImportError:
    pass
try:
    import numpy as np
    _l_(57660)

except ImportError:
    pass
sr1 = _c_(57663, _a_(57662, _n_(57661, "pd", lambda: pd), "Series"), [1, 2, 3, 4, 5])
_l_(57664)
sr2 = _c_(57667, _a_(57666, _n_(57665, "pd", lambda: pd), "Series"), [2, 4, 6, 8, 10])
_l_(57668)
_c_(57670, _n_(57669, "print", lambda: print), 'Original Series:')
_l_(57671)
_c_(57673, _n_(57672, "print", lambda: print), 'sr1:')
_l_(57674)
_c_(57677, _n_(57675, "print", lambda: print), _n_(57676, "sr1", lambda: sr1))
_l_(57678)
_c_(57680, _n_(57679, "print", lambda: print), 'sr2:')
_l_(57681)
_c_(57684, _n_(57682, "print", lambda: print), _n_(57683, "sr2", lambda: sr2))
_l_(57685)
_c_(57687, _n_(57686, "print", lambda: print), '\nItems of a given series not present in another given series:')
_l_(57688)
sr22 = _c_(57696, _a_(57690, _n_(57689, "pd", lambda: pd), "Series"), _c_(57695, _a_(57692, _n_(57691, "np", lambda: np), "intersect1d"), _n_(57693, "sr1", lambda: sr1), _n_(57694, "sr2", lambda: sr2)))
_l_(57697)
result = _n_(57698, "sr11", lambda: sr11)[~_c_(57702, _a_(57700, _n_(57699, "sr11", lambda: sr11), "isin"), _n_(57701, "sr22", lambda: sr22))]
_l_(57703)
_c_(57706, _n_(57704, "print", lambda: print), _n_(57705, "result", lambda: result))
_l_(57707)