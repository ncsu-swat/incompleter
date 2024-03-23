# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(52716)

except ImportError:
    pass
_c_(52718, _n_(52717, "print", lambda: print), 'Create a dataframe, indexing by date and time:')
_l_(52719)
df_dt = _c_(52723, _a_(52721, _n_(52720, "pd", lambda: pd), "DataFrame"), {'Sale_amt': [100, 110, 117, 150, 112, 99, 129, 135, 140, 150]}, index=_n_(52722, "dt_range", lambda: dt_range))
_l_(52724)
_c_(52727, _n_(52725, "print", lambda: print), _n_(52726, "df_dt", lambda: df_dt))
_l_(52728)