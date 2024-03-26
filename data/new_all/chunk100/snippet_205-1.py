# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(105008)

except ImportError:
    pass
_c_(105010, _n_(105009, "print", lambda: print), 'Sequences of fixed-frequency dates and time spans (1 H):\n')
_l_(105011)
_c_(105014, _n_(105012, "print", lambda: print), _n_(105013, "r1", lambda: r1))
_l_(105015)
_c_(105017, _n_(105016, "print", lambda: print), '\nSequences of fixed-frequency dates and time spans (3 H):\n')
_l_(105018)
r2 = _c_(105021, _a_(105020, _n_(105019, "pd", lambda: pd), "date_range"), '2030-01-01', periods=10, freq='3H')
_l_(105022)
_c_(105025, _n_(105023, "print", lambda: print), _n_(105024, "r2", lambda: r2))
_l_(105026)