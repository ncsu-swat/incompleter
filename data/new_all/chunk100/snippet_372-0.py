# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(112900)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(112902)

except ImportError:
    pass
_c_(112904, _n_(112903, "print", lambda: print), 'Original Numpy array:')
_l_(112905)
_c_(112908, _n_(112906, "print", lambda: print), _n_(112907, "np_array", lambda: np_array))
_l_(112909)
_c_(112914, _n_(112910, "print", lambda: print), 'Type: ', _c_(112913, _n_(112911, "type", lambda: type), _n_(112912, "np_array", lambda: np_array)))
_l_(112915)
df = _c_(112922, _a_(112917, _n_(112916, "pd", lambda: pd), "DataFrame"), _c_(112921, _a_(112920, _a_(112919, _n_(112918, "np", lambda: np), "random"), "rand"), 12, 3), columns=['A', 'B', 'C'])
_l_(112923)
_c_(112925, _n_(112924, "print", lambda: print), "\nPanda's DataFrame: ")
_l_(112926)
_c_(112929, _n_(112927, "print", lambda: print), _n_(112928, "df", lambda: df))
_l_(112930)
_c_(112935, _n_(112931, "print", lambda: print), 'Type: ', _c_(112934, _n_(112932, "type", lambda: type), _n_(112933, "df", lambda: df)))
_l_(112936)