# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/434287/how-to-iterate-over-a-list-in-chunks
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import more_itertools
    _l_(1541169)

except ImportError:
    pass
for s in _c_(1541174, _a_(1541171, _n_(1541170, "more_itertools", lambda: more_itertools), "chunked"), _c_(1541173, _n_(1541172, "range", lambda: range), 9), 4):
    _l_(1541179)

    _c_(1541177, _n_(1541175, "print", lambda: print), _n_(1541176, "s", lambda: s))
    _l_(1541178)

[0, 1, 2, 3]
_l_(1541180)
[4, 5, 6, 7]
_l_(1541181)
[8]
_l_(1541182)

