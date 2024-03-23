# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(15293)

except ImportError:
    pass
_c_(15295, _n_(15294, "print", lambda: print), 'Original DataFrame:')
_l_(15296)
_c_(15299, _n_(15297, "print", lambda: print), _n_(15298, "df", lambda: df))
_l_(15300)
_c_(15302, _n_(15301, "print", lambda: print), '\nLength of the string in a column:')
_l_(15303)
_n_(15304, "df", lambda: df)['company_code_length'] = _c_(15308, _a_(15306, _n_(15305, "df", lambda: df)['company_code'], "apply"), _n_(15307, "len", lambda: len))
_l_(15309)
_c_(15312, _n_(15310, "print", lambda: print), _n_(15311, "df", lambda: df))
_l_(15313)