# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import collections
    _l_(73545)

except ImportError:
    pass
try:
    import pprint
    _l_(73547)

except ImportError:
    pass
with _c_(73550, _n_(73548, "open", lambda: open), _n_(73549, "file_input", lambda: file_input), 'r') as info:
    _l_(73565)

    count = _c_(73558, _a_(73552, _n_(73551, "collections", lambda: collections), "Counter"), _c_(73557, _a_(73556, _c_(73555, _a_(73554, _n_(73553, "info", lambda: info), "read")), "upper")))
    _l_(73559)
    value = _c_(73563, _a_(73561, _n_(73560, "pprint", lambda: pprint), "pformat"), _n_(73562, "count", lambda: count))
    _l_(73564)
_c_(73568, _n_(73566, "print", lambda: print), _n_(73567, "value", lambda: value))
_l_(73569)