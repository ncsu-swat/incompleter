# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/152580/whats-the-canonical-way-to-check-for-type-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from typeguard import check_type
    _l_(65189)

except ImportError:
    pass
try:
    from typing import List
    _l_(65191)

except ImportError:
    pass

try:
    _l_(65203)

    _c_(65195, _n_(65192, "check_type", lambda: check_type), 'mylist', [1, 2], _n_(65193, "List", lambda: List)[_n_(65194, "int", lambda: int)])
    _l_(65196)
except _n_(65197, "TypeError", lambda: TypeError) as e:
    _l_(65202)

    _c_(65200, _n_(65198, "print", lambda: print), _n_(65199, "e", lambda: e))
    _l_(65201)

_c_(65209, _n_(65204, "check_type", lambda: check_type), 'foo', [1, 3.14], _n_(65205, "List", lambda: List)[_n_(65206, "Union", lambda: Union)[_n_(65207, "int", lambda: int), _n_(65208, "float", lambda: float)]])
_l_(65210)
# vs
_c_(65214, _n_(65211, "isinstance", lambda: isinstance), _n_(65212, "foo", lambda: foo), _n_(65213, "list", lambda: list)) and _c_(65222, _n_(65215, "all", lambda: all), (_c_(65220, _n_(65216, "isinstance", lambda: isinstance), _n_(65217, "a", lambda: a), (_n_(65218, "int", lambda: int), _n_(65219, "float", lambda: float))) for a in _n_(65221, "foo", lambda: foo))) 
_l_(65223) 

