# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import re
    _l_(112481)

except ImportError:
    pass
x = True
_l_(112482)
while _n_(112483, "x", lambda: x):
    _l_(112527)

    if _c_(112486, _n_(112484, "len", lambda: len), _n_(112485, "p", lambda: p)) < 6 or _c_(112489, _n_(112487, "len", lambda: len), _n_(112488, "p", lambda: p)) > 12:
        _l_(112526)

        break
        _l_(112490)
    elif not _c_(112494, _a_(112492, _n_(112491, "re", lambda: re), "search"), '[a-z]', _n_(112493, "p", lambda: p)):
        _l_(112525)

        break
        _l_(112495)
    elif not _c_(112499, _a_(112497, _n_(112496, "re", lambda: re), "search"), '[0-9]', _n_(112498, "p", lambda: p)):
        _l_(112524)

        break
        _l_(112500)
    elif not _c_(112504, _a_(112502, _n_(112501, "re", lambda: re), "search"), '[A-Z]', _n_(112503, "p", lambda: p)):
        _l_(112523)

        break
        _l_(112505)
    elif not _c_(112509, _a_(112507, _n_(112506, "re", lambda: re), "search"), '[$#@]', _n_(112508, "p", lambda: p)):
        _l_(112522)

        break
        _l_(112510)
    elif _c_(112514, _a_(112512, _n_(112511, "re", lambda: re), "search"), '\\s', _n_(112513, "p", lambda: p)):
        _l_(112521)

        break
        _l_(112515)
    else:
        _c_(112517, _n_(112516, "print", lambda: print), 'Valid Password')
        _l_(112518)
        x = False
        _l_(112519)
        break
        _l_(112520)
if _n_(112528, "x", lambda: x):
    _l_(112532)

    _c_(112530, _n_(112529, "print", lambda: print), 'Not a Valid Password')
    _l_(112531)