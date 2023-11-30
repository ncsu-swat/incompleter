# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/38987/how-do-i-merge-two-dictionaries-in-a-single-expression
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import Counter
    _l_(1548023)

except ImportError:
    pass
dict1 = {'a':1, 'b': 2}
_l_(1548024)
dict2 = {'b':10, 'c': 11}
_l_(1548025)
result = _c_(1548033, _n_(1548026, "dict", lambda: dict), _c_(1548029, _n_(1548027, "Counter", lambda: Counter), _n_(1548028, "dict1", lambda: dict1)) + _c_(1548032, _n_(1548030, "Counter", lambda: Counter), _n_(1548031, "dict2", lambda: dict2)))
_l_(1548034)

