# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(35156)

except ImportError:
    pass
try:
    import numpy as np
    _l_(35158)

except ImportError:
    pass
_c_(35162, _a_(35161, _a_(35160, _n_(35159, "np", lambda: np), "random"), "seed"), 24)
_l_(35163)
df = _c_(35169, _a_(35165, _n_(35164, "pd", lambda: pd), "DataFrame"), {'A': _c_(35168, _a_(35167, _n_(35166, "np", lambda: np), "linspace"), 1, 10, 10)})
_l_(35170)
_a_(35172, _n_(35171, "df", lambda: df), "iloc")[0, 2] = _a_(35174, _n_(35173, "np", lambda: np), "nan")
_l_(35175)
_a_(35177, _n_(35176, "df", lambda: df), "iloc")[3, 3] = _a_(35179, _n_(35178, "np", lambda: np), "nan")
_l_(35180)
_a_(35182, _n_(35181, "df", lambda: df), "iloc")[4, 1] = _a_(35184, _n_(35183, "np", lambda: np), "nan")
_l_(35185)
_a_(35187, _n_(35186, "df", lambda: df), "iloc")[9, 4] = _a_(35189, _n_(35188, "np", lambda: np), "nan")
_l_(35190)
_c_(35192, _n_(35191, "print", lambda: print), 'Original array:')
_l_(35193)
_c_(35196, _n_(35194, "print", lambda: print), _n_(35195, "df", lambda: df))
_l_(35197)

def highlight_cols(s):
    _l_(35201)

    color = 'grey'
    _l_(35198)
    aux = 'background-color: %s' % _n_(35199, "color", lambda: color)
    _l_(35200)
    return aux
_c_(35203, _n_(35202, "print", lambda: print), '\nHighlight specific columns:')
_l_(35204)
_c_(35211, _a_(35207, _a_(35206, _n_(35205, "df", lambda: df), "style"), "applymap"), _n_(35208, "highlight_cols", lambda: highlight_cols), subset=_a_(35210, _n_(35209, "pd", lambda: pd), "IndexSlice")[:, ['B', 'C']])
_l_(35212)