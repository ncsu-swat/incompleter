# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53005229/typeerror-a-bytes-like-object-is-required-not-str-in-run-line-line-split
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
with _c_(441566, _n_(441564, "open", lambda: open), _n_(441565, "fname", lambda: fname), 'rb') as f:
    _l_(441574)

    lines = [_c_(441569, _a_(441568, _n_(441567, "x", lambda: x), "strip")) for x in _c_(441572, _a_(441571, _n_(441570, "f", lambda: f), "readlines"))]
    _l_(441573)

for line in _n_(441575, "lines", lambda: lines):
    _l_(441584)

    tmp = _c_(441580, _a_(441579, _c_(441578, _a_(441577, _n_(441576, "line", lambda: line), "strip")), "lower"))
    _l_(441581)
    if 'some-pattern' in _n_(441582, "tmp", lambda: tmp):
        _l_(441583)

