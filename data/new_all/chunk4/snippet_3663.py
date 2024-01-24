# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70348607/typeerror-unsupported-operand-types-for-str-and-str-pandas-reindex
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(638404)

except ImportError:
    pass
s1=_c_(638409, _a_(638406, _n_(638405, "pd", lambda: pd), "Series"), [1,2,3,4],index=_c_(638408, _n_(638407, "list", lambda: list), 'aceg'))
_l_(638410)
_c_(638420, _n_(638411, "print", lambda: print), _c_(638419, _a_(638413, _n_(638412, "s1", lambda: s1), "reindex"), _c_(638418, _a_(638415, _n_(638414, "pd", lambda: pd), "Index"), _c_(638417, _n_(638416, "list", lambda: list), 'abdg')),method='nearest'))
_l_(638421)