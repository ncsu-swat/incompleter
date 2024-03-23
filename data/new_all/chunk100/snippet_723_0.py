# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import collections
    _l_(73501)

except ImportError:
    pass
try:
    import pprint
    _l_(73503)

except ImportError:
    pass
file_input = _c_(73505, _n_(73504, "input", lambda: input), 'File Name: ')
_l_(73506)
with _c_(73509, _n_(73507, "open", lambda: open), _n_(73508, "file_input", lambda: file_input), 'r') as info:
    _l_(73519)

    count = _c_(73517, _a_(73511, _n_(73510, "collections", lambda: collections), "Counter"), _c_(73516, _a_(73515, _c_(73514, _a_(73513, _n_(73512, "info", lambda: info), "read")), "upper")))
    _l_(73518)
_c_(73522, _n_(73520, "print", lambda: print), _n_(73521, "value", lambda: value))
_l_(73523)