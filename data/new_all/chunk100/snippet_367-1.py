# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import re
    _l_(112534)

except ImportError:
    pass
p = _c_(112536, _n_(112535, "input", lambda: input), 'Input your password')
_l_(112537)
while _n_(112538, "x", lambda: x):
    _l_(112582)

    if _c_(112541, _n_(112539, "len", lambda: len), _n_(112540, "p", lambda: p)) < 6 or _c_(112544, _n_(112542, "len", lambda: len), _n_(112543, "p", lambda: p)) > 12:
        _l_(112581)

        break
        _l_(112545)
    elif not _c_(112549, _a_(112547, _n_(112546, "re", lambda: re), "search"), '[a-z]', _n_(112548, "p", lambda: p)):
        _l_(112580)

        break
        _l_(112550)
    elif not _c_(112554, _a_(112552, _n_(112551, "re", lambda: re), "search"), '[0-9]', _n_(112553, "p", lambda: p)):
        _l_(112579)

        break
        _l_(112555)
    elif not _c_(112559, _a_(112557, _n_(112556, "re", lambda: re), "search"), '[A-Z]', _n_(112558, "p", lambda: p)):
        _l_(112578)

        break
        _l_(112560)
    elif not _c_(112564, _a_(112562, _n_(112561, "re", lambda: re), "search"), '[$#@]', _n_(112563, "p", lambda: p)):
        _l_(112577)

        break
        _l_(112565)
    elif _c_(112569, _a_(112567, _n_(112566, "re", lambda: re), "search"), '\\s', _n_(112568, "p", lambda: p)):
        _l_(112576)

        break
        _l_(112570)
    else:
        _c_(112572, _n_(112571, "print", lambda: print), 'Valid Password')
        _l_(112573)
        x = False
        _l_(112574)
        break
        _l_(112575)
if _n_(112583, "x", lambda: x):
    _l_(112587)

    _c_(112585, _n_(112584, "print", lambda: print), 'Not a Valid Password')
    _l_(112586)