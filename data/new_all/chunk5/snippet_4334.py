# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59541629/typeerror-input-y-of-mul-op-has-type-float32-that-does-not-match-type-int32
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(705785)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(705787)

except ImportError:
    pass
try:
    import tensorflow as tf
    _l_(705789)

except ImportError:
    pass
w = _c_(705794, _a_(705791, _n_(705790, "tf", lambda: tf), "Variable"), 0, dtype=_a_(705793, _n_(705792, "tf", lambda: tf), "float32"))
_l_(705795)
cost = _c_(705806, _a_(705797, _n_(705796, "tf", lambda: tf), "add"), _c_(705805, _a_(705799, _n_(705798, "tf", lambda: tf), "add"), _n_(705800, "w", lambda: w)**2, _c_(705804, _a_(705802, _n_(705801, "tf", lambda: tf), "multiply"), -10,_n_(705803, "w", lambda: w))), 25)
_l_(705807)
train = _c_(705814, _a_(705812, _c_(705811, _a_(705810, _a_(705809, _n_(705808, "tf", lambda: tf), "train"), "GradientDescentOptimizer"), 0.001), "minimize"), _n_(705813, "cost", lambda: cost))
_l_(705815)

init = _c_(705818, _a_(705817, _n_(705816, "tf", lambda: tf), "global_variables_initializer"))
_l_(705819)
session = _c_(705822, _a_(705821, _n_(705820, "tf", lambda: tf), "session"))
_l_(705823)
_c_(705827, _a_(705825, _n_(705824, "session", lambda: session), "run"), _n_(705826, "init", lambda: init))
_l_(705828)
_c_(705832, _a_(705830, _n_(705829, "session", lambda: session), "run"), _n_(705831, "w", lambda: w))
_l_(705833)