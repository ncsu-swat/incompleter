# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(8352)

except ImportError:
    pass
try:
    import numpy as np
    _l_(8354)

except ImportError:
    pass
_c_(8358, _a_(8357, _a_(8356, _n_(8355, "np", lambda: np), "random"), "seed"), 24)
_l_(8359)
df = _c_(8365, _a_(8361, _n_(8360, "pd", lambda: pd), "DataFrame"), {'A': _c_(8364, _a_(8363, _n_(8362, "np", lambda: np), "linspace"), 1, 10, 10)})
_l_(8366)
_a_(8368, _n_(8367, "df", lambda: df), "iloc")[0, 2] = _a_(8370, _n_(8369, "np", lambda: np), "nan")
_l_(8371)
_a_(8373, _n_(8372, "df", lambda: df), "iloc")[3, 3] = _a_(8375, _n_(8374, "np", lambda: np), "nan")
_l_(8376)
_a_(8378, _n_(8377, "df", lambda: df), "iloc")[4, 1] = _a_(8380, _n_(8379, "np", lambda: np), "nan")
_l_(8381)
_a_(8383, _n_(8382, "df", lambda: df), "iloc")[9, 4] = _a_(8385, _n_(8384, "np", lambda: np), "nan")
_l_(8386)
_c_(8388, _n_(8387, "print", lambda: print), 'Original array:')
_l_(8389)
_c_(8392, _n_(8390, "print", lambda: print), _n_(8391, "df", lambda: df))
_l_(8393)
_c_(8395, _n_(8394, "print", lambda: print), '\nBar charts in dataframe:')
_l_(8396)
_c_(8400, _a_(8399, _a_(8398, _n_(8397, "df", lambda: df), "style"), "bar"), subset=['B', 'C'], color='#d65f5f')
_l_(8401)