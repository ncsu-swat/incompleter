# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def test(str1):
    _l_(50647)

    result = [_c_(50637, _n_(50635, "int", lambda: int), _n_(50636, "str1", lambda: str1)) for str1 in _c_(50640, _a_(50639, _n_(50638, "str1", lambda: str1), "split")) if _c_(50643, _a_(50642, _n_(50641, "str1", lambda: str1), "isdigit"))]
    _l_(50644)
    aux = _n_(50645, "result", lambda: result)
    _l_(50646)
    return aux
_c_(50650, _n_(50648, "print", lambda: print), 'Original string:', _n_(50649, "str1", lambda: str1))
_l_(50651)
_c_(50653, _n_(50652, "print", lambda: print), 'Extract numbers from the said string:')
_l_(50654)
_c_(50659, _n_(50655, "print", lambda: print), _c_(50658, _n_(50656, "test", lambda: test), _n_(50657, "str1", lambda: str1)))
_l_(50660)