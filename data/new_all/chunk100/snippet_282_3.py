# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def substring_copy(str, n):
    _l_(22869)

    if _n_(22847, "flen", lambda: flen) > _c_(22850, _n_(22848, "len", lambda: len), _n_(22849, "str", lambda: str)):
        _l_(22855)

        flen = _c_(22853, _n_(22851, "len", lambda: len), _n_(22852, "str", lambda: str))
        _l_(22854)
    substr = _n_(22856, "str", lambda: str)[:_n_(22857, "flen", lambda: flen)]
    _l_(22858)
    result = ''
    _l_(22859)
    for i in _c_(22862, _n_(22860, "range", lambda: range), _n_(22861, "n", lambda: n)):
        _l_(22866)

        result = _n_(22863, "result", lambda: result) + _n_(22864, "substr", lambda: substr)
        _l_(22865)
    aux = _n_(22867, "result", lambda: result)
    _l_(22868)
    return aux
_c_(22873, _n_(22870, "print", lambda: print), _c_(22872, _n_(22871, "substring_copy", lambda: substring_copy), 'abcdef', 2))
_l_(22874)
_c_(22878, _n_(22875, "print", lambda: print), _c_(22877, _n_(22876, "substring_copy", lambda: substring_copy), 'p', 3))
_l_(22879)