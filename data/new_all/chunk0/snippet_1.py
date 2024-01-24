# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/33054527/typeerror-a-bytes-like-object-is-required-not-str-when-handling-file-conte
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
with _c_(48318, _n_(48316, "open", lambda: open), _n_(48317, "fname", lambda: fname), 'rb') as f:
    _l_(48326)

    lines = [_c_(48321, _a_(48320, _n_(48319, "x", lambda: x), "strip")) for x in _c_(48324, _a_(48323, _n_(48322, "f", lambda: f), "readlines"))]
    _l_(48325)

for line in _n_(48327, "lines", lambda: lines):
    _l_(48336)

    tmp = _c_(48332, _a_(48331, _c_(48330, _a_(48329, _n_(48328, "line", lambda: line), "strip")), "lower"))
    _l_(48333)
    if 'some-pattern' in _n_(48334, "tmp", lambda: tmp):
        _l_(48335)

