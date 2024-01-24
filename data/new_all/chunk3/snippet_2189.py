# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59020487/getting-typeerror-trying-to-open-a-file-in-write-mode-with-python
# [omitting some setup]

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
with _c_(548165, _n_(548163, "open", lambda: open), _n_(548164, "setFile", lambda: setFile), 'r') as setFile:
    _l_(548170)

    olddata = _c_(548168, _a_(548167, _n_(548166, "setFile", lambda: setFile), "readlines"))
    _l_(548169)

newdata = ''
_l_(548171)

for line in _n_(548172, "olddata", lambda: olddata):
    _l_(548180)

    newdata += _c_(548178, _a_(548174, _n_(548173, "re", lambda: re), "sub"), _n_(548175, "regex", lambda: regex), _n_(548176, "newset", lambda: newset), _n_(548177, "line", lambda: line))
    _l_(548179)

with _c_(548183, _n_(548181, "open", lambda: open), _n_(548182, "setFile", lambda: setFile), 'w') as setFile:
    _l_(548189)

    _c_(548187, _a_(548185, _n_(548184, "setFile", lambda: setFile), "write"), _n_(548186, "newdata", lambda: newdata))
    _l_(548188)