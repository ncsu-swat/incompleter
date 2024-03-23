# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(67400)

except ImportError:
    pass
sr1 = _c_(67403, _a_(67402, _n_(67401, "pd", lambda: pd), "Series"), [1, 2, 3, 4, 5])
_l_(67404)
_c_(67406, _n_(67405, "print", lambda: print), 'Original Series:')
_l_(67407)
_c_(67409, _n_(67408, "print", lambda: print), 'sr1:')
_l_(67410)
_c_(67413, _n_(67411, "print", lambda: print), _n_(67412, "sr1", lambda: sr1))
_l_(67414)
_c_(67416, _n_(67415, "print", lambda: print), 'sr2:')
_l_(67417)
_c_(67420, _n_(67418, "print", lambda: print), _n_(67419, "sr2", lambda: sr2))
_l_(67421)
_c_(67423, _n_(67422, "print", lambda: print), '\nItems of sr1 not present in sr2:')
_l_(67424)
result = _n_(67425, "sr1", lambda: sr1)[~_c_(67429, _a_(67427, _n_(67426, "sr1", lambda: sr1), "isin"), _n_(67428, "sr2", lambda: sr2))]
_l_(67430)
_c_(67433, _n_(67431, "print", lambda: print), _n_(67432, "result", lambda: result))
_l_(67434)