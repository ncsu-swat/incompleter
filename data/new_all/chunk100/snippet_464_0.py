# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def printValues():
    _l_(49116)

    for i in _c_(49101, _n_(49100, "range", lambda: range), 1, 21):
        _l_(49107)

        _c_(49105, _a_(49103, _n_(49102, "l", lambda: l), "append"), _n_(49104, "i", lambda: i) ** 2)
        _l_(49106)
    _c_(49110, _n_(49108, "print", lambda: print), _n_(49109, "l", lambda: l)[:5])
    _l_(49111)
    _c_(49114, _n_(49112, "print", lambda: print), _n_(49113, "l", lambda: l)[-5:])
    _l_(49115)
_c_(49118, _n_(49117, "printValues", lambda: printValues))
_l_(49119)