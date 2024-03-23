# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(15969)

except ImportError:
    pass
_c_(15971, _n_(15970, "print", lambda: print), 'Sequences of fixed-frequency dates and time spans (1 H):\n')
_l_(15972)
r1 = _c_(15975, _a_(15974, _n_(15973, "pd", lambda: pd), "date_range"), '2030-01-01', periods=10, freq='H')
_l_(15976)
_c_(15979, _n_(15977, "print", lambda: print), _n_(15978, "r1", lambda: r1))
_l_(15980)
_c_(15982, _n_(15981, "print", lambda: print), '\nSequences of fixed-frequency dates and time spans (3 H):\n')
_l_(15983)
_c_(15986, _n_(15984, "print", lambda: print), _n_(15985, "r2", lambda: r2))
_l_(15987)