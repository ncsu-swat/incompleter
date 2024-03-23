# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(39219)

except ImportError:
    pass
_c_(39221, _n_(39220, "print", lambda: print), 'Original DataFrame:')
_l_(39222)
_c_(39225, _n_(39223, "print", lambda: print), _n_(39224, "df", lambda: df))
_l_(39226)
_c_(39228, _n_(39227, "print", lambda: print), '\nIs proper case or title case?')
_l_(39229)
_n_(39230, "df", lambda: df)['company_code_is_title'] = _c_(39238, _n_(39231, "list", lambda: list), _c_(39237, _n_(39232, "map", lambda: map), lambda x: _c_(39235, _a_(39234, _n_(39233, "x", lambda: x), "istitle")), _n_(39236, "df", lambda: df)['company_code']))
_l_(39239)
_c_(39242, _n_(39240, "print", lambda: print), _n_(39241, "df", lambda: df))
_l_(39243)