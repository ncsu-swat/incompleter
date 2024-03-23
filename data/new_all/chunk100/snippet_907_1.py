# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(91109)

except ImportError:
    pass
try:
    from collections import Counter
    _l_(91111)

except ImportError:
    pass
color_series = _c_(91114, _a_(91113, _n_(91112, "pd", lambda: pd), "Series"), ['Red', 'Green', 'Orange', 'Pink', 'Yellow', 'White'])
_l_(91115)
_c_(91117, _n_(91116, "print", lambda: print), 'Original Series:')
_l_(91118)
_c_(91121, _n_(91119, "print", lambda: print), _n_(91120, "color_series", lambda: color_series))
_l_(91122)
_c_(91124, _n_(91123, "print", lambda: print), '\nFiltered words:')
_l_(91125)
_c_(91129, _n_(91126, "print", lambda: print), _n_(91127, "color_series", lambda: color_series)[_n_(91128, "result", lambda: result)])
_l_(91130)