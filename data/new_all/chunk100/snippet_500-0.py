# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(119018)

except ImportError:
    pass
_c_(119020, _n_(119019, "print", lambda: print), 'Original DataFrame:')
_l_(119021)
_c_(119024, _n_(119022, "print", lambda: print), _n_(119023, "df", lambda: df))
_l_(119025)
_c_(119027, _n_(119026, "print", lambda: print), '\nLength of sale_amount:')
_l_(119028)
_n_(119029, "df", lambda: df)['sale_amount_length'] = _c_(119036, _a_(119034, _c_(119033, _a_(119031, _n_(119030, "df", lambda: df)['sale_amount'], "map"), _n_(119032, "str", lambda: str)), "apply"), _n_(119035, "len", lambda: len))
_l_(119037)
_c_(119040, _n_(119038, "print", lambda: print), _n_(119039, "df", lambda: df))
_l_(119041)