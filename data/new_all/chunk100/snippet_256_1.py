# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(20237, _n_(20236, "print", lambda: print), 'Original dictionary:')
_l_(20238)
_c_(20241, _n_(20239, "print", lambda: print), _n_(20240, "d", lambda: d))
_l_(20242)
_c_(20247, _n_(20243, "print", lambda: print), _c_(20246, _n_(20244, "type", lambda: type), _n_(20245, "d", lambda: d)))
_l_(20248)
try:
    import json
    _l_(20250)

except ImportError:
    pass
with _c_(20252, _n_(20251, "open", lambda: open), 'dictionary', 'w') as f:
    _l_(20259)

    _c_(20257, _a_(20254, _n_(20253, "json", lambda: json), "dump"), _n_(20255, "d", lambda: d), _n_(20256, "f", lambda: f), indent=4, sort_keys=True)
    _l_(20258)
_c_(20261, _n_(20260, "print", lambda: print), '\nJson file to dictionary:')
_l_(20262)
with _c_(20264, _n_(20263, "open", lambda: open), 'dictionary') as f:
    _l_(20270)

    data = _c_(20268, _a_(20266, _n_(20265, "json", lambda: json), "load"), _n_(20267, "f", lambda: f))
    _l_(20269)
_c_(20273, _n_(20271, "print", lambda: print), _n_(20272, "data", lambda: data))
_l_(20274)