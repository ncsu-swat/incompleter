# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(15949)

except ImportError:
    pass
_c_(15951, _n_(15950, "print", lambda: print), 'Sequences of fixed-frequency dates and time spans (1 H):\n')
_l_(15952)
_c_(15955, _n_(15953, "print", lambda: print), _n_(15954, "r1", lambda: r1))
_l_(15956)
_c_(15958, _n_(15957, "print", lambda: print), '\nSequences of fixed-frequency dates and time spans (3 H):\n')
_l_(15959)
r2 = _c_(15962, _a_(15961, _n_(15960, "pd", lambda: pd), "date_range"), '2030-01-01', periods=10, freq='3H')
_l_(15963)
_c_(15966, _n_(15964, "print", lambda: print), _n_(15965, "r2", lambda: r2))
_l_(15967)