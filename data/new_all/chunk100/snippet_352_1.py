# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import json
    _l_(35070)

except ImportError:
    pass
_c_(35072, _n_(35071, "print", lambda: print), 'Original Python object:')
_l_(35073)
_c_(35076, _n_(35074, "print", lambda: print), _n_(35075, "python_obj", lambda: python_obj))
_l_(35077)
json_obj = _c_(35081, _a_(35079, _n_(35078, "json", lambda: json), "loads"), _n_(35080, "python_obj", lambda: python_obj))
_l_(35082)
_c_(35084, _n_(35083, "print", lambda: print), '\nUnique Key in a JSON object:')
_l_(35085)
_c_(35088, _n_(35086, "print", lambda: print), _n_(35087, "json_obj", lambda: json_obj))
_l_(35089)