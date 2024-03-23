# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(5658)

except ImportError:
    pass
_c_(5660, _n_(5659, "print", lambda: print), 'Original DataFrame:')
_l_(5661)
_c_(5664, _n_(5662, "print", lambda: print), _n_(5663, "df", lambda: df))
_l_(5665)
_c_(5667, _n_(5666, "print", lambda: print), '\nReplace A with c:')
_l_(5668)
df = _c_(5671, _a_(5670, _n_(5669, "df", lambda: df), "replace"), 'A', 'C')
_l_(5672)
_c_(5675, _n_(5673, "print", lambda: print), _n_(5674, "df", lambda: df))
_l_(5676)