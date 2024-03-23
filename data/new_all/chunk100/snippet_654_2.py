# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(67436)

except ImportError:
    pass
sr2 = _c_(67439, _a_(67438, _n_(67437, "pd", lambda: pd), "Series"), [2, 4, 6, 8, 10])
_l_(67440)
_c_(67442, _n_(67441, "print", lambda: print), 'Original Series:')
_l_(67443)
_c_(67445, _n_(67444, "print", lambda: print), 'sr1:')
_l_(67446)
_c_(67449, _n_(67447, "print", lambda: print), _n_(67448, "sr1", lambda: sr1))
_l_(67450)
_c_(67452, _n_(67451, "print", lambda: print), 'sr2:')
_l_(67453)
_c_(67456, _n_(67454, "print", lambda: print), _n_(67455, "sr2", lambda: sr2))
_l_(67457)
_c_(67459, _n_(67458, "print", lambda: print), '\nItems of sr1 not present in sr2:')
_l_(67460)
result = _n_(67461, "sr1", lambda: sr1)[~_c_(67465, _a_(67463, _n_(67462, "sr1", lambda: sr1), "isin"), _n_(67464, "sr2", lambda: sr2))]
_l_(67466)
_c_(67469, _n_(67467, "print", lambda: print), _n_(67468, "result", lambda: result))
_l_(67470)