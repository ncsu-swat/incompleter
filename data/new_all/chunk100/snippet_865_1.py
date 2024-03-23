# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(85436)

except ImportError:
    pass
_c_(85438, _n_(85437, "print", lambda: print), 'Original DataFrame:')
_l_(85439)
_c_(85442, _n_(85440, "print", lambda: print), _n_(85441, "df", lambda: df))
_l_(85443)
_a_(85445, _n_(85444, "df", lambda: df), "index").name = 'Index_name'
_l_(85446)
_c_(85448, _n_(85447, "print", lambda: print), '\nSaid DataFrame with a title or name of the index column:')
_l_(85449)
_c_(85452, _n_(85450, "print", lambda: print), _n_(85451, "df", lambda: df))
_l_(85453)