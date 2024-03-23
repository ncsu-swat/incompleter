# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(52730)

except ImportError:
    pass
_c_(52732, _n_(52731, "print", lambda: print), 'Create a dataframe, indexing by date and time:')
_l_(52733)
dt_range = _c_(52736, _a_(52735, _n_(52734, "pd", lambda: pd), "date_range"), start='2020-05-12 07:10:10', freq='S', periods=10)
_l_(52737)
_c_(52740, _n_(52738, "print", lambda: print), _n_(52739, "df_dt", lambda: df_dt))
_l_(52741)