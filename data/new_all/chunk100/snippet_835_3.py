# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(83191)

except ImportError:
    pass
try:
    import numpy as np
    _l_(83193)

except ImportError:
    pass
sales_tuples = _c_(83198, _n_(83194, "list", lambda: list), _c_(83197, _n_(83195, "zip", lambda: zip), *_n_(83196, "sales_arrays", lambda: sales_arrays)))
_l_(83199)
_c_(83201, _n_(83200, "print", lambda: print), 'Create a MultiIndex:')
_l_(83202)
sales_index = _c_(83207, _a_(83205, _a_(83204, _n_(83203, "pd", lambda: pd), "MultiIndex"), "from_tuples"), _n_(83206, "sales_tuples", lambda: sales_tuples), names=['sale', 'city'])
_l_(83208)
_c_(83211, _n_(83209, "print", lambda: print), _n_(83210, "sales_tuples", lambda: sales_tuples))
_l_(83212)
_c_(83214, _n_(83213, "print", lambda: print), '\nConstruct a series using the said MultiIndex levels: ')
_l_(83215)
s = _c_(83223, _a_(83217, _n_(83216, "pd", lambda: pd), "Series"), _c_(83221, _a_(83220, _a_(83219, _n_(83218, "np", lambda: np), "random"), "randn"), 8), index=_n_(83222, "sales_index", lambda: sales_index))
_l_(83224)
_c_(83227, _n_(83225, "print", lambda: print), _n_(83226, "s", lambda: s))
_l_(83228)