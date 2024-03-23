# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import re
    _l_(36028)

except ImportError:
    pass
p = _c_(36030, _n_(36029, "input", lambda: input), 'Input your password')
_l_(36031)
while _n_(36032, "x", lambda: x):
    _l_(36076)

    if _c_(36035, _n_(36033, "len", lambda: len), _n_(36034, "p", lambda: p)) < 6 or _c_(36038, _n_(36036, "len", lambda: len), _n_(36037, "p", lambda: p)) > 12:
        _l_(36075)

        break
        _l_(36039)
    elif not _c_(36043, _a_(36041, _n_(36040, "re", lambda: re), "search"), '[a-z]', _n_(36042, "p", lambda: p)):
        _l_(36074)

        break
        _l_(36044)
    elif not _c_(36048, _a_(36046, _n_(36045, "re", lambda: re), "search"), '[0-9]', _n_(36047, "p", lambda: p)):
        _l_(36073)

        break
        _l_(36049)
    elif not _c_(36053, _a_(36051, _n_(36050, "re", lambda: re), "search"), '[A-Z]', _n_(36052, "p", lambda: p)):
        _l_(36072)

        break
        _l_(36054)
    elif not _c_(36058, _a_(36056, _n_(36055, "re", lambda: re), "search"), '[$#@]', _n_(36057, "p", lambda: p)):
        _l_(36071)

        break
        _l_(36059)
    elif _c_(36063, _a_(36061, _n_(36060, "re", lambda: re), "search"), '\\s', _n_(36062, "p", lambda: p)):
        _l_(36070)

        break
        _l_(36064)
    else:
        _c_(36066, _n_(36065, "print", lambda: print), 'Valid Password')
        _l_(36067)
        x = False
        _l_(36068)
        break
        _l_(36069)
if _n_(36077, "x", lambda: x):
    _l_(36081)

    _c_(36079, _n_(36078, "print", lambda: print), 'Not a Valid Password')
    _l_(36080)