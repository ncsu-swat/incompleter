# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59578283/tensorflow-probability-attributeerror-module-tensorflow-probability-has-no
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(392941)

except ImportError:
    pass
try:
    import tensorflow.compat.v2 as tf
    _l_(392943)

except ImportError:
    pass
try:
    import tensorflow_probability as tfp
    _l_(392945)

except ImportError:
    pass
tfb = _a_(392947, _n_(392946, "tfp", lambda: tfp), "bijectors")
_l_(392948)
tfd = _a_(392950, _n_(392949, "tfp", lambda: tfp), "distributions")
_l_(392951)
_c_(392954, _a_(392953, _n_(392952, "tf", lambda: tf), "enable_v2_behavior"))
_l_(392955)

constrain_positive = _c_(392968, _c_(392964, _a_(392957, _n_(392956, "tfb", lambda: tfb), "Shift"), _a_(392963, _c_(392962, _a_(392959, _n_(392958, "np", lambda: np), "finfo"), _a_(392961, _n_(392960, "np", lambda: np), "float64")), "tiny")), _c_(392967, _a_(392966, _n_(392965, "tfb", lambda: tfb), "Exp")))
_l_(392969)

amplitude_var = _c_(392976, _a_(392972, _a_(392971, _n_(392970, "tfp", lambda: tfp), "util"), "TransformedVariable"), initial_value=1.,
    bijector=_n_(392973, "constrain_positive", lambda: constrain_positive),
    name='amplitude',
    dtype=_a_(392975, _n_(392974, "np", lambda: np), "float64"))
_l_(392977)