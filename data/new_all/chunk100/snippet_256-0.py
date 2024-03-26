# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(107043, _n_(107042, "print", lambda: print), 'Original dictionary:')
_l_(107044)
_c_(107047, _n_(107045, "print", lambda: print), _n_(107046, "d", lambda: d))
_l_(107048)
_c_(107053, _n_(107049, "print", lambda: print), _c_(107052, _n_(107050, "type", lambda: type), _n_(107051, "d", lambda: d)))
_l_(107054)
try:
    import json
    _l_(107056)

except ImportError:
    pass
with _c_(107058, _n_(107057, "open", lambda: open), 'dictionary', 'w') as f:
    _l_(107065)

    _c_(107063, _a_(107060, _n_(107059, "json", lambda: json), "dump"), _n_(107061, "d", lambda: d), _n_(107062, "f", lambda: f), indent=4, sort_keys=True)
    _l_(107064)
_c_(107067, _n_(107066, "print", lambda: print), '\nJson file to dictionary:')
_l_(107068)
with _c_(107070, _n_(107069, "open", lambda: open), 'dictionary') as f:
    _l_(107076)

    data = _c_(107074, _a_(107072, _n_(107071, "json", lambda: json), "load"), _n_(107073, "f", lambda: f))
    _l_(107075)
_c_(107079, _n_(107077, "print", lambda: print), _n_(107078, "data", lambda: data))
_l_(107080)