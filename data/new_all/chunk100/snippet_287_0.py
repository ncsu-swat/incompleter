# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(24519)

except ImportError:
    pass
_c_(24521, _n_(24520, "print", lambda: print), 'Original DataFrame:')
_l_(24522)
_c_(24525, _n_(24523, "print", lambda: print), _n_(24524, "df", lambda: df))
_l_(24526)
_c_(24528, _n_(24527, "print", lambda: print), '\nTitle cases:')
_l_(24529)
_n_(24530, "df", lambda: df)['company_code_title_cases'] = _c_(24538, _n_(24531, "list", lambda: list), _c_(24537, _n_(24532, "map", lambda: map), lambda x: _c_(24535, _a_(24534, _n_(24533, "x", lambda: x), "title")), _n_(24536, "df", lambda: df)['company_code']))
_l_(24539)
_c_(24542, _n_(24540, "print", lambda: print), _n_(24541, "df", lambda: df))
_l_(24543)