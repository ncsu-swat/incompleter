# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(115367)

except ImportError:
    pass
num_series = _c_(115372, _a_(115369, _n_(115368, "pd", lambda: pd), "Series"), _c_(115371, _n_(115370, "list", lambda: list), '2390238923902390239023'))
_l_(115373)
_c_(115375, _n_(115374, "print", lambda: print), 'Original Series:')
_l_(115376)
_c_(115379, _n_(115377, "print", lambda: print), _n_(115378, "num_series", lambda: num_series))
_l_(115380)
result = _c_(115384, _a_(115382, _n_(115381, "num_series", lambda: num_series), "take"), _n_(115383, "element_pos", lambda: element_pos))
_l_(115385)
_c_(115387, _n_(115386, "print", lambda: print), '\nExtract items at given positions of the said series:')
_l_(115388)
_c_(115391, _n_(115389, "print", lambda: print), _n_(115390, "result", lambda: result))
_l_(115392)