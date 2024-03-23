# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import re
    _l_(36083)

except ImportError:
    pass
x = True
_l_(36084)
while _n_(36085, "x", lambda: x):
    _l_(36129)

    if _c_(36088, _n_(36086, "len", lambda: len), _n_(36087, "p", lambda: p)) < 6 or _c_(36091, _n_(36089, "len", lambda: len), _n_(36090, "p", lambda: p)) > 12:
        _l_(36128)

        break
        _l_(36092)
    elif not _c_(36096, _a_(36094, _n_(36093, "re", lambda: re), "search"), '[a-z]', _n_(36095, "p", lambda: p)):
        _l_(36127)

        break
        _l_(36097)
    elif not _c_(36101, _a_(36099, _n_(36098, "re", lambda: re), "search"), '[0-9]', _n_(36100, "p", lambda: p)):
        _l_(36126)

        break
        _l_(36102)
    elif not _c_(36106, _a_(36104, _n_(36103, "re", lambda: re), "search"), '[A-Z]', _n_(36105, "p", lambda: p)):
        _l_(36125)

        break
        _l_(36107)
    elif not _c_(36111, _a_(36109, _n_(36108, "re", lambda: re), "search"), '[$#@]', _n_(36110, "p", lambda: p)):
        _l_(36124)

        break
        _l_(36112)
    elif _c_(36116, _a_(36114, _n_(36113, "re", lambda: re), "search"), '\\s', _n_(36115, "p", lambda: p)):
        _l_(36123)

        break
        _l_(36117)
    else:
        _c_(36119, _n_(36118, "print", lambda: print), 'Valid Password')
        _l_(36120)
        x = False
        _l_(36121)
        break
        _l_(36122)
if _n_(36130, "x", lambda: x):
    _l_(36134)

    _c_(36132, _n_(36131, "print", lambda: print), 'Not a Valid Password')
    _l_(36133)