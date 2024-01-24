# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64025453/attributeerror-rangeindex-object-has-no-attribute-inferred-freq
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from statsmodels.tsa.seasonal import seasonal_decompose
    _l_(396517)

except ImportError:
    pass
decomposition = _c_(396520, _n_(396518, "seasonal_decompose", lambda: seasonal_decompose), _n_(396519, "ts_log", lambda: ts_log))
_l_(396521)

trend = _a_(396523, _n_(396522, "decomposition", lambda: decomposition), "trend")
_l_(396524)
seasonal = _a_(396526, _n_(396525, "decomposition", lambda: decomposition), "seasonal")
_l_(396527)
residual = _a_(396529, _n_(396528, "decomposition", lambda: decomposition), "resid")
_l_(396530)