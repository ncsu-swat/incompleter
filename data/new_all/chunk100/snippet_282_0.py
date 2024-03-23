# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def substring_copy(str, n):
    _l_(22805)

    flen = 2
    _l_(22783)
    if _n_(22784, "flen", lambda: flen) > _c_(22787, _n_(22785, "len", lambda: len), _n_(22786, "str", lambda: str)):
        _l_(22792)

        flen = _c_(22790, _n_(22788, "len", lambda: len), _n_(22789, "str", lambda: str))
        _l_(22791)
    substr = _n_(22793, "str", lambda: str)[:_n_(22794, "flen", lambda: flen)]
    _l_(22795)
    for i in _c_(22798, _n_(22796, "range", lambda: range), _n_(22797, "n", lambda: n)):
        _l_(22802)

        result = _n_(22799, "result", lambda: result) + _n_(22800, "substr", lambda: substr)
        _l_(22801)
    aux = _n_(22803, "result", lambda: result)
    _l_(22804)
    return aux
_c_(22809, _n_(22806, "print", lambda: print), _c_(22808, _n_(22807, "substring_copy", lambda: substring_copy), 'abcdef', 2))
_l_(22810)
_c_(22814, _n_(22811, "print", lambda: print), _c_(22813, _n_(22812, "substring_copy", lambda: substring_copy), 'p', 3))
_l_(22815)