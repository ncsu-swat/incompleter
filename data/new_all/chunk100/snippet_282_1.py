# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def substring_copy(str, n):
    _l_(22836)

    flen = 2
    _l_(22816)
    if _n_(22817, "flen", lambda: flen) > _c_(22820, _n_(22818, "len", lambda: len), _n_(22819, "str", lambda: str)):
        _l_(22825)

        flen = _c_(22823, _n_(22821, "len", lambda: len), _n_(22822, "str", lambda: str))
        _l_(22824)
    result = ''
    _l_(22826)
    for i in _c_(22829, _n_(22827, "range", lambda: range), _n_(22828, "n", lambda: n)):
        _l_(22833)

        result = _n_(22830, "result", lambda: result) + _n_(22831, "substr", lambda: substr)
        _l_(22832)
    aux = _n_(22834, "result", lambda: result)
    _l_(22835)
    return aux
_c_(22840, _n_(22837, "print", lambda: print), _c_(22839, _n_(22838, "substring_copy", lambda: substring_copy), 'abcdef', 2))
_l_(22841)
_c_(22845, _n_(22842, "print", lambda: print), _c_(22844, _n_(22843, "substring_copy", lambda: substring_copy), 'p', 3))
_l_(22846)