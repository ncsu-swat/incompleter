# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import collections
    _l_(73525)

except ImportError:
    pass
try:
    import pprint
    _l_(73527)

except ImportError:
    pass
file_input = _c_(73529, _n_(73528, "input", lambda: input), 'File Name: ')
_l_(73530)
with _c_(73533, _n_(73531, "open", lambda: open), _n_(73532, "file_input", lambda: file_input), 'r') as info:
    _l_(73539)

    value = _c_(73537, _a_(73535, _n_(73534, "pprint", lambda: pprint), "pformat"), _n_(73536, "count", lambda: count))
    _l_(73538)
_c_(73542, _n_(73540, "print", lambda: print), _n_(73541, "value", lambda: value))
_l_(73543)