# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(33380)

except ImportError:
    pass
_c_(33382, _n_(33381, "print", lambda: print), 'Original DataFrame with single index:')
_l_(33383)
_c_(33386, _n_(33384, "print", lambda: print), _n_(33385, "df", lambda: df))
_l_(33387)
_c_(33389, _n_(33388, "print", lambda: print), '\nDataFrame without index:')
_l_(33390)
_c_(33395, _n_(33391, "print", lambda: print), _c_(33394, _a_(33393, _n_(33392, "df", lambda: df), "to_string"), index=False))
_l_(33396)