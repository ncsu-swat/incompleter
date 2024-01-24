# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/33054527/typeerror-a-bytes-like-object-is-required-not-str-when-handling-file-conte
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
with _c_(387807, _n_(387805, "open", lambda: open), _n_(387806, "fname", lambda: fname), 'rb') as f:
    _l_(387815)

    lines = [_c_(387810, _a_(387809, _n_(387808, "x", lambda: x), "strip")) for x in _c_(387813, _a_(387812, _n_(387811, "f", lambda: f), "readlines"))]
    _l_(387814)

for line in _n_(387816, "lines", lambda: lines):
    _l_(387825)

    tmp = _c_(387821, _a_(387820, _c_(387819, _a_(387818, _n_(387817, "line", lambda: line), "strip")), "lower"))
    _l_(387822)
    if 'some-pattern' in _n_(387823, "tmp", lambda: tmp):
        _l_(387824)

