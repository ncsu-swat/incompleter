# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(8294)

except ImportError:
    pass
try:
    import numpy as np
    _l_(8296)

except ImportError:
    pass
_c_(8300, _a_(8299, _a_(8298, _n_(8297, "np", lambda: np), "random"), "seed"), 24)
_l_(8301)
df = _c_(8314, _a_(8303, _n_(8302, "pd", lambda: pd), "concat"), [_n_(8304, "df", lambda: df), _c_(8313, _a_(8306, _n_(8305, "pd", lambda: pd), "DataFrame"), _c_(8310, _a_(8309, _a_(8308, _n_(8307, "np", lambda: np), "random"), "randn"), 10, 4), columns=_c_(8312, _n_(8311, "list", lambda: list), 'BCDE'))], axis=1)
_l_(8315)
_a_(8317, _n_(8316, "df", lambda: df), "iloc")[0, 2] = _a_(8319, _n_(8318, "np", lambda: np), "nan")
_l_(8320)
_a_(8322, _n_(8321, "df", lambda: df), "iloc")[3, 3] = _a_(8324, _n_(8323, "np", lambda: np), "nan")
_l_(8325)
_a_(8327, _n_(8326, "df", lambda: df), "iloc")[4, 1] = _a_(8329, _n_(8328, "np", lambda: np), "nan")
_l_(8330)
_a_(8332, _n_(8331, "df", lambda: df), "iloc")[9, 4] = _a_(8334, _n_(8333, "np", lambda: np), "nan")
_l_(8335)
_c_(8337, _n_(8336, "print", lambda: print), 'Original array:')
_l_(8338)
_c_(8341, _n_(8339, "print", lambda: print), _n_(8340, "df", lambda: df))
_l_(8342)
_c_(8344, _n_(8343, "print", lambda: print), '\nBar charts in dataframe:')
_l_(8345)
_c_(8349, _a_(8348, _a_(8347, _n_(8346, "df", lambda: df), "style"), "bar"), subset=['B', 'C'], color='#d65f5f')
_l_(8350)