# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(67366)

except ImportError:
    pass
sr1 = _c_(67369, _a_(67368, _n_(67367, "pd", lambda: pd), "Series"), [1, 2, 3, 4, 5])
_l_(67370)
sr2 = _c_(67373, _a_(67372, _n_(67371, "pd", lambda: pd), "Series"), [2, 4, 6, 8, 10])
_l_(67374)
_c_(67376, _n_(67375, "print", lambda: print), 'Original Series:')
_l_(67377)
_c_(67379, _n_(67378, "print", lambda: print), 'sr1:')
_l_(67380)
_c_(67383, _n_(67381, "print", lambda: print), _n_(67382, "sr1", lambda: sr1))
_l_(67384)
_c_(67386, _n_(67385, "print", lambda: print), 'sr2:')
_l_(67387)
_c_(67390, _n_(67388, "print", lambda: print), _n_(67389, "sr2", lambda: sr2))
_l_(67391)
_c_(67393, _n_(67392, "print", lambda: print), '\nItems of sr1 not present in sr2:')
_l_(67394)
_c_(67397, _n_(67395, "print", lambda: print), _n_(67396, "result", lambda: result))
_l_(67398)