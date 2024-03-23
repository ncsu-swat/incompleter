# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import OrderedDict
    _l_(53253)

except ImportError:
    pass
new_dict = _c_(53258, _n_(53254, "OrderedDict", lambda: OrderedDict), _c_(53257, _a_(53256, _n_(53255, "dict", lambda: dict), "items")))
_l_(53259)
for key in _n_(53260, "new_dict", lambda: new_dict):
    _l_(53267)

    _c_(53265, _n_(53261, "print", lambda: print), _n_(53262, "key", lambda: key), _n_(53263, "new_dict", lambda: new_dict)[_n_(53264, "key", lambda: key)])
    _l_(53266)
_c_(53269, _n_(53268, "print", lambda: print), '\nIn reverse order:')
_l_(53270)
for key in _c_(53273, _n_(53271, "reversed", lambda: reversed), _n_(53272, "new_dict", lambda: new_dict)):
    _l_(53280)

    _c_(53278, _n_(53274, "print", lambda: print), _n_(53275, "key", lambda: key), _n_(53276, "new_dict", lambda: new_dict)[_n_(53277, "key", lambda: key)])
    _l_(53279)