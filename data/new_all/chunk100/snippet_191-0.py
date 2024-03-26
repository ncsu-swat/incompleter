# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(104222)

except ImportError:
    pass
_c_(104224, _n_(104223, "print", lambda: print), 'Original DataFrame:')
_l_(104225)
_c_(104228, _n_(104226, "print", lambda: print), _n_(104227, "df", lambda: df))
_l_(104229)
_c_(104231, _n_(104230, "print", lambda: print), '\nLength of the string in a column:')
_l_(104232)
_n_(104233, "df", lambda: df)['company_code_length'] = _c_(104237, _a_(104235, _n_(104234, "df", lambda: df)['company_code'], "apply"), _n_(104236, "len", lambda: len))
_l_(104238)
_c_(104241, _n_(104239, "print", lambda: print), _n_(104240, "df", lambda: df))
_l_(104242)