# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(104988)

except ImportError:
    pass
_c_(104990, _n_(104989, "print", lambda: print), 'Sequences of fixed-frequency dates and time spans (1 H):\n')
_l_(104991)
r1 = _c_(104994, _a_(104993, _n_(104992, "pd", lambda: pd), "date_range"), '2030-01-01', periods=10, freq='H')
_l_(104995)
_c_(104998, _n_(104996, "print", lambda: print), _n_(104997, "r1", lambda: r1))
_l_(104999)
_c_(105001, _n_(105000, "print", lambda: print), '\nSequences of fixed-frequency dates and time spans (3 H):\n')
_l_(105002)
_c_(105005, _n_(105003, "print", lambda: print), _n_(105004, "r2", lambda: r2))
_l_(105006)