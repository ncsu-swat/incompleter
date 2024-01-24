# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/45132645/list-comprehension-in-exec-with-empty-locals-nameerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def bar():
    _l_(413277)

    aux = 1
    _l_(413276)
    return aux
_c_(413283, _n_(413278, "print", lambda: print), [_c_(413280, _n_(413279, "bar", lambda: bar)) for _ in _c_(413282, _n_(413281, "range", lambda: range), 5)])
_l_(413284)