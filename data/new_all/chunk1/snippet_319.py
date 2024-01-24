# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/23187916/base64-type-err-typeerror-expected-bytes-not-str
#!/usr/bin/python3.2

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import time, sys, os
    _l_(401430)

except ImportError:
    pass
try:
    import base64
    _l_(401432)

except ImportError:
    pass
#####################
tmp = "/home/gh.txt"
_l_(401433)
ex = "/home/ex.txt"
_l_(401434)
if (_c_(401438, _n_(401435, "len", lambda: len), _a_(401437, _n_(401436, "sys", lambda: sys), "argv")) < 2):
    _l_(401450)

    _c_(401440, _n_(401439, "print", lambda: print), "enter name of the new dict and key")
    _l_(401441)
else:
    global ns
    _l_(401442)
    ns = _a_(401444, _n_(401443, "sys", lambda: sys), "argv")[1]
    _l_(401445)
    global ps
    _l_(401446)
    ps = _a_(401448, _n_(401447, "sys", lambda: sys), "argv")[2]
    _l_(401449)

dss = "{<%s>:%s}" % (_n_(401451, "ns", lambda: ns), _n_(401452, "ps", lambda: ps))
_l_(401453)
_c_(401456, _a_(401455, _n_(401454, "os", lambda: os), "system"), "touch dss0")
_l_(401457)
fi0 = _c_(401460, _n_(401458, "open", lambda: open), _n_(401459, "tmp", lambda: tmp), "a")
_l_(401461)

_c_(401465, _a_(401463, _n_(401462, "fi0", lambda: fi0), "write"), _n_(401464, "dss", lambda: dss))
_l_(401466)
d64i = _c_(401470, _a_(401468, _n_(401467, "base64", lambda: base64), "b64encode"), _n_(401469, "tmp", lambda: tmp))
_l_(401471)
fi = _c_(401474, _n_(401472, "open", lambda: open), _n_(401473, "ex", lambda: ex), "a")
_l_(401475)
_c_(401479, _a_(401477, _n_(401476, "fi", lambda: fi), "write"), _n_(401478, "d64i", lambda: d64i))
_l_(401480)
_c_(401483, _a_(401482, _n_(401481, "os", lambda: os), "system"), "rm tmp")
_l_(401484)