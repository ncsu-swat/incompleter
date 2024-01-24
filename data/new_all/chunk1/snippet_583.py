# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75580189/filter-none-value-from-python-list-returns-typeerror-boolean-value-of-na-is-am
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(386401)

except ImportError:
    pass
x = _c_(386404, _a_(386403, _n_(386402, "pd", lambda: pd), "array"), ['This is', 'some text', None, 'data.'], dtype="string")
_l_(386405)
x = _c_(386410, _n_(386406, "list", lambda: list), _c_(386409, _a_(386408, _n_(386407, "x", lambda: x), "unique")))
_l_(386411)
_c_(386416, _n_(386412, "list", lambda: list), _c_(386415, _n_(386413, "filter", lambda: filter), None, _n_(386414, "x", lambda: x)))
_l_(386417)