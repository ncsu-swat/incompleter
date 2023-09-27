# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/16138232/is-it-a-good-practice-to-use-try-except-else-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
d = _c_(1541866, _n_(1541865, "dict", lambda: dict))
_l_(1541867)
try:
    _l_(1541873)

    item = _n_(1541868, "d", lambda: d)['item']
    _l_(1541869)
except _n_(1541870, "KeyError", lambda: KeyError):
    _l_(1541872)

    item = 'default'
    _l_(1541871)

item = _c_(1541876, _a_(1541875, _n_(1541874, "d", lambda: d), "get"), 'item', 'default')
_l_(1541877)

