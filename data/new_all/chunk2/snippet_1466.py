# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55592445/how-to-resolve-nameerror-when-importing-class-with-class-variables-that-depend-o
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class foo:
    _l_(425805)

    A = 5
    _l_(425799)
    B = [_n_(425800, "i", lambda: i)*_n_(425801, "A", lambda: A) for A in _c_(425803, _n_(425802, "range", lambda: range), 3)]
    _l_(425804)