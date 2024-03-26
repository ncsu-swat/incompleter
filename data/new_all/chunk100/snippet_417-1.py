# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(115394)

except ImportError:
    pass
element_pos = [0, 2, 6, 11, 21]
_l_(115395)
_c_(115397, _n_(115396, "print", lambda: print), 'Original Series:')
_l_(115398)
_c_(115401, _n_(115399, "print", lambda: print), _n_(115400, "num_series", lambda: num_series))
_l_(115402)
result = _c_(115406, _a_(115404, _n_(115403, "num_series", lambda: num_series), "take"), _n_(115405, "element_pos", lambda: element_pos))
_l_(115407)
_c_(115409, _n_(115408, "print", lambda: print), '\nExtract items at given positions of the said series:')
_l_(115410)
_c_(115413, _n_(115411, "print", lambda: print), _n_(115412, "result", lambda: result))
_l_(115414)