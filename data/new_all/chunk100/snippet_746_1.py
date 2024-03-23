# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(75371)

except ImportError:
    pass
try:
    import numpy as np
    _l_(75373)

except ImportError:
    pass
_c_(75377, _a_(75376, _a_(75375, _n_(75374, "np", lambda: np), "random"), "seed"), 24)
_l_(75378)
df = _c_(75384, _a_(75380, _n_(75379, "pd", lambda: pd), "DataFrame"), {'A': _c_(75383, _a_(75382, _n_(75381, "np", lambda: np), "linspace"), 1, 10, 10)})
_l_(75385)
_a_(75387, _n_(75386, "df", lambda: df), "iloc")[0, 2] = _a_(75389, _n_(75388, "np", lambda: np), "nan")
_l_(75390)
_a_(75392, _n_(75391, "df", lambda: df), "iloc")[3, 3] = _a_(75394, _n_(75393, "np", lambda: np), "nan")
_l_(75395)
_a_(75397, _n_(75396, "df", lambda: df), "iloc")[4, 1] = _a_(75399, _n_(75398, "np", lambda: np), "nan")
_l_(75400)
_a_(75402, _n_(75401, "df", lambda: df), "iloc")[9, 4] = _a_(75404, _n_(75403, "np", lambda: np), "nan")
_l_(75405)
_c_(75407, _n_(75406, "print", lambda: print), 'Original array:')
_l_(75408)
_c_(75411, _n_(75409, "print", lambda: print), _n_(75410, "df", lambda: df))
_l_(75412)
_c_(75414, _n_(75413, "print", lambda: print), '\nDataframe - table style and border around the table and not around the rows:')
_l_(75415)
_c_(75419, _a_(75418, _a_(75417, _n_(75416, "df", lambda: df), "style"), "set_table_styles"), [{'selector': '', 'props': [('border', '4px solid #7a7')]}])
_l_(75420)