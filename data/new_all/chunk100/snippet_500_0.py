# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(52132)

except ImportError:
    pass
_c_(52134, _n_(52133, "print", lambda: print), 'Original DataFrame:')
_l_(52135)
_c_(52138, _n_(52136, "print", lambda: print), _n_(52137, "df", lambda: df))
_l_(52139)
_c_(52141, _n_(52140, "print", lambda: print), '\nLength of sale_amount:')
_l_(52142)
_n_(52143, "df", lambda: df)['sale_amount_length'] = _c_(52150, _a_(52148, _c_(52147, _a_(52145, _n_(52144, "df", lambda: df)['sale_amount'], "map"), _n_(52146, "str", lambda: str)), "apply"), _n_(52149, "len", lambda: len))
_l_(52151)
_c_(52154, _n_(52152, "print", lambda: print), _n_(52153, "df", lambda: df))
_l_(52155)