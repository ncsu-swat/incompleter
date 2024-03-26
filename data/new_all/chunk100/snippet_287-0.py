# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(108624)

except ImportError:
    pass
_c_(108626, _n_(108625, "print", lambda: print), 'Original DataFrame:')
_l_(108627)
_c_(108630, _n_(108628, "print", lambda: print), _n_(108629, "df", lambda: df))
_l_(108631)
_c_(108633, _n_(108632, "print", lambda: print), '\nTitle cases:')
_l_(108634)
_n_(108635, "df", lambda: df)['company_code_title_cases'] = _c_(108643, _n_(108636, "list", lambda: list), _c_(108642, _n_(108637, "map", lambda: map), lambda x: _c_(108640, _a_(108639, _n_(108638, "x", lambda: x), "title")), _n_(108641, "df", lambda: df)['company_code']))
_l_(108644)
_c_(108647, _n_(108645, "print", lambda: print), _n_(108646, "df", lambda: df))
_l_(108648)