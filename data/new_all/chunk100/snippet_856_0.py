# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(84573)

except ImportError:
    pass
_c_(84575, _n_(84574, "print", lambda: print), 'Original DataFrame:')
_l_(84576)
_c_(84579, _n_(84577, "print", lambda: print), _n_(84578, "df", lambda: df))
_l_(84580)
_c_(84582, _n_(84581, "print", lambda: print), '\nIf a specified column starts with a specified string?')
_l_(84583)
_n_(84584, "df", lambda: df)['company_code_starts_with'] = _c_(84592, _n_(84585, "list", lambda: list), _c_(84591, _n_(84586, "map", lambda: map), lambda x: _c_(84589, _a_(84588, _n_(84587, "x", lambda: x), "startswith"), 'ze'), _n_(84590, "df", lambda: df)['company_code']))
_l_(84593)
_c_(84596, _n_(84594, "print", lambda: print), _n_(84595, "df", lambda: df))
_l_(84597)