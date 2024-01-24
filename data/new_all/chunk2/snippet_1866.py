# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/41236090/attributeerror-module-tensorflow-python-summary-summary-has-no-attribute-sca
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tensorflow as tf
    _l_(421558)

except ImportError:
    pass
x = _c_(421564, _a_(421560, _n_(421559, "tf", lambda: tf), "Variable"), _c_(421563, _a_(421562, _n_(421561, "tf", lambda: tf), "random_normal"), 5,5))
_l_(421565)
_c_(421570, _a_(421568, _a_(421567, _n_(421566, "tf", lambda: tf), "summary"), "scalar"), 'input', _n_(421569, "x", lambda: x))
_l_(421571)