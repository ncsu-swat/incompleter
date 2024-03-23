# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(41046)

except ImportError:
    pass
element_pos = [0, 2, 6, 11, 21]
_l_(41047)
_c_(41049, _n_(41048, "print", lambda: print), 'Original Series:')
_l_(41050)
_c_(41053, _n_(41051, "print", lambda: print), _n_(41052, "num_series", lambda: num_series))
_l_(41054)
result = _c_(41058, _a_(41056, _n_(41055, "num_series", lambda: num_series), "take"), _n_(41057, "element_pos", lambda: element_pos))
_l_(41059)
_c_(41061, _n_(41060, "print", lambda: print), '\nExtract items at given positions of the said series:')
_l_(41062)
_c_(41065, _n_(41063, "print", lambda: print), _n_(41064, "result", lambda: result))
_l_(41066)