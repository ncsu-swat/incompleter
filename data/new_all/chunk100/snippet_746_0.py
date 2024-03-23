# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(75313)

except ImportError:
    pass
try:
    import numpy as np
    _l_(75315)

except ImportError:
    pass
_c_(75319, _a_(75318, _a_(75317, _n_(75316, "np", lambda: np), "random"), "seed"), 24)
_l_(75320)
df = _c_(75333, _a_(75322, _n_(75321, "pd", lambda: pd), "concat"), [_n_(75323, "df", lambda: df), _c_(75332, _a_(75325, _n_(75324, "pd", lambda: pd), "DataFrame"), _c_(75329, _a_(75328, _a_(75327, _n_(75326, "np", lambda: np), "random"), "randn"), 10, 4), columns=_c_(75331, _n_(75330, "list", lambda: list), 'BCDE'))], axis=1)
_l_(75334)
_a_(75336, _n_(75335, "df", lambda: df), "iloc")[0, 2] = _a_(75338, _n_(75337, "np", lambda: np), "nan")
_l_(75339)
_a_(75341, _n_(75340, "df", lambda: df), "iloc")[3, 3] = _a_(75343, _n_(75342, "np", lambda: np), "nan")
_l_(75344)
_a_(75346, _n_(75345, "df", lambda: df), "iloc")[4, 1] = _a_(75348, _n_(75347, "np", lambda: np), "nan")
_l_(75349)
_a_(75351, _n_(75350, "df", lambda: df), "iloc")[9, 4] = _a_(75353, _n_(75352, "np", lambda: np), "nan")
_l_(75354)
_c_(75356, _n_(75355, "print", lambda: print), 'Original array:')
_l_(75357)
_c_(75360, _n_(75358, "print", lambda: print), _n_(75359, "df", lambda: df))
_l_(75361)
_c_(75363, _n_(75362, "print", lambda: print), '\nDataframe - table style and border around the table and not around the rows:')
_l_(75364)
_c_(75368, _a_(75367, _a_(75366, _n_(75365, "df", lambda: df), "style"), "set_table_styles"), [{'selector': '', 'props': [('border', '4px solid #7a7')]}])
_l_(75369)