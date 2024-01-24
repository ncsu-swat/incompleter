# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/45209678/attributeerror-module-tensorflow-has-no-attribute-select
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tensorflow as tf
    _l_(472059)

except ImportError:
    pass
try:
    import numpy as np
    _l_(472061)

except ImportError:
    pass

A = 3
_l_(472062)
B = _c_(472065, _a_(472064, _n_(472063, "tf", lambda: tf), "convert_to_tensor"), [1, 2, 3, 4])
_l_(472066)
C = _c_(472069, _a_(472068, _n_(472067, "tf", lambda: tf), "convert_to_tensor"), [1, 1, 1, 1])
_l_(472070)
D = _c_(472073, _a_(472072, _n_(472071, "tf", lambda: tf), "convert_to_tensor"), [0, 0, 0, 0])
_l_(472074)

with _c_(472077, _a_(472076, _n_(472075, "tf", lambda: tf), "Session")) as sess:
    _l_(472109)

    _c_(472086, _n_(472078, "print", lambda: print), _c_(472085, _a_(472080, _n_(472079, "sess", lambda: sess), "run"), _c_(472084, _a_(472082, _n_(472081, "tf", lambda: tf), "select"), _n_(472083, "A", lambda: A) > 1, 'A', 'B')))
    _l_(472087)
    _c_(472095, _n_(472088, "print", lambda: print), _c_(472094, _a_(472090, _n_(472089, "sess", lambda: sess), "run"), _c_(472093, _a_(472092, _n_(472091, "tf", lambda: tf), "select"), False, 'A', 'B')))
    _l_(472096)
    _c_(472107, _n_(472097, "print", lambda: print), _c_(472106, _a_(472099, _n_(472098, "sess", lambda: sess), "run"), _c_(472105, _a_(472101, _n_(472100, "tf", lambda: tf), "select"), _n_(472102, "B", lambda: B) > 2, _n_(472103, "C", lambda: C), _n_(472104, "D", lambda: D))))
    _l_(472108)