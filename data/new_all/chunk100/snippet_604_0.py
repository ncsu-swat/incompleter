# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(63289)

except ImportError:
    pass
_c_(63291, _n_(63290, "print", lambda: print), 'Original DataFrame:')
_l_(63292)
_c_(63295, _n_(63293, "print", lambda: print), _n_(63294, "df", lambda: df))
_l_(63296)
_c_(63298, _n_(63297, "print", lambda: print), '\nSwapp cases in comapny_code:')
_l_(63299)
_n_(63300, "df", lambda: df)['swapped_company_code'] = _c_(63308, _n_(63301, "list", lambda: list), _c_(63307, _n_(63302, "map", lambda: map), lambda x: _c_(63305, _a_(63304, _n_(63303, "x", lambda: x), "swapcase")), _n_(63306, "df", lambda: df)['company_code']))
_l_(63309)
_c_(63312, _n_(63310, "print", lambda: print), _n_(63311, "df", lambda: df))
_l_(63313)