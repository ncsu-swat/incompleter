# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74549909/bentoml-localhost-server-returns-with-typeerror-runnermethod-object-is-not-ca
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(450709)

except ImportError:
    pass
try:
    import bentoml
    _l_(450711)

except ImportError:
    pass
try:
    from bentoml.io import NumpyNdarray
    _l_(450713)

except ImportError:
    pass

BENTO_MODEL_TAG = "mmrt_model:p2ya6otlggzx4me4"
_l_(450714)

estimator_runner = _c_(450721, _a_(450720, _c_(450719, _a_(450717, _a_(450716, _n_(450715, "bentoml", lambda: bentoml), "keras"), "get"), _n_(450718, "BENTO_MODEL_TAG", lambda: BENTO_MODEL_TAG)), "to_runner"))
_l_(450722)

MMRT_service = _c_(450726, _a_(450724, _n_(450723, "bentoml", lambda: bentoml), "Service"), "MMRT_Estimator", runners=[_n_(450725, "estimator_runner", lambda: estimator_runner)])
_l_(450727)

@_c_(450733, _a_(450729, _n_(450728, "MMRT_service", lambda: MMRT_service), "api"), input=_c_(450731, _n_(450730, "NumpyNdarray", lambda: NumpyNdarray)), output=_n_(450732, "float", lambda: float))
def predict(input_data: _a_(450735, _n_(450734, "np", lambda: np), "ndarray")) -> _n_(450736, "float", lambda: float):
    _l_(450742)

    aux = _c_(450740, _a_(450738, _n_(450737, "estimator_runner", lambda: estimator_runner), "predict"), _n_(450739, "input_data", lambda: input_data))
    _l_(450741)
    return aux