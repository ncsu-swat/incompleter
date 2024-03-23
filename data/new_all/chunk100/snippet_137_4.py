# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(9244)

except ImportError:
    pass
try:
    import numpy as np
    _l_(9246)

except ImportError:
    pass
sales_arrays = [['sale1', 'sale1', 'sale3', 'sale3', 'sale2', 'sale2', 'sale4', 'sale4'], ['city1', 'city2', 'city1', 'city2', 'city1', 'city2', 'city1', 'city2']]
_l_(9247)
sales_tuples = _c_(9252, _n_(9248, "list", lambda: list), _c_(9251, _n_(9249, "zip", lambda: zip), *_n_(9250, "sales_arrays", lambda: sales_arrays)))
_l_(9253)
sales_index = _c_(9258, _a_(9256, _a_(9255, _n_(9254, "pd", lambda: pd), "MultiIndex"), "from_tuples"), _n_(9257, "sales_tuples", lambda: sales_tuples), names=['sale', 'city'])
_l_(9259)
_c_(9261, _n_(9260, "print", lambda: print), '\nConstruct a Dataframe using the said MultiIndex levels:')
_l_(9262)
_c_(9265, _n_(9263, "print", lambda: print), _n_(9264, "df", lambda: df))
_l_(9266)
_c_(9268, _n_(9267, "print", lambda: print), '\nSelect 1st, 2nd and 3rd row of the said DataFrame:')
_l_(9269)
positions = [1, 2, 5]
_l_(9270)
_c_(9275, _n_(9271, "print", lambda: print), _c_(9274, _a_(9273, _n_(9272, "df", lambda: df), "take"), [1, 2, 5]))
_l_(9276)
_c_(9278, _n_(9277, "print", lambda: print), '\nTake elements at indices 1 and 2 along the axis 1 (column selection):')
_l_(9279)
_c_(9284, _n_(9280, "print", lambda: print), _c_(9283, _a_(9282, _n_(9281, "df", lambda: df), "take"), [1, 2], axis=1))
_l_(9285)
_c_(9287, _n_(9286, "print", lambda: print), '\nTake elements at indices 4 and 3 using negative integers along the axis 1 (column selection):')
_l_(9288)
_c_(9293, _n_(9289, "print", lambda: print), _c_(9292, _a_(9291, _n_(9290, "df", lambda: df), "take"), [-1, -2], axis=1))
_l_(9294)