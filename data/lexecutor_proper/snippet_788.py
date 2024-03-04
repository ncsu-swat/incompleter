# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/26646362/numpy-array-is-not-json-serializable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import json
    _l_(64945)

except ImportError:
    pass
try:
    import numpy as np
    _l_(64947)

except ImportError:
    pass

class NumpyEncoder(_a_(64949, _n_(64948, "json", lambda: json), "JSONEncoder")):
    _l_(64988)

    """ Special json encoder for numpy types """
    def default(self, obj):
        _l_(64987)

        if _c_(64954, _n_(64950, "isinstance", lambda: isinstance), _n_(64951, "obj", lambda: obj), _a_(64953, _n_(64952, "np", lambda: np), "integer")):
            _l_(64979)

            aux = _c_(64957, _n_(64955, "int", lambda: int), _n_(64956, "obj", lambda: obj))
            _l_(64958)
            return aux
        elif _c_(64963, _n_(64959, "isinstance", lambda: isinstance), _n_(64960, "obj", lambda: obj), _a_(64962, _n_(64961, "np", lambda: np), "floating")):
            _l_(64978)

            aux = _c_(64966, _n_(64964, "float", lambda: float), _n_(64965, "obj", lambda: obj))
            _l_(64967)
            return aux
        elif _c_(64972, _n_(64968, "isinstance", lambda: isinstance), _n_(64969, "obj", lambda: obj), _a_(64971, _n_(64970, "np", lambda: np), "ndarray")):
            _l_(64977)

            aux = _c_(64975, _a_(64974, _n_(64973, "obj", lambda: obj), "tolist"))
            _l_(64976)
            return aux
        aux = _c_(64985, _a_(64982, _a_(64981, _n_(64980, "json", lambda: json), "JSONEncoder"), "default"), _n_(64983, "self", lambda: self), _n_(64984, "obj", lambda: obj))
        _l_(64986)
        return aux

dumped = _c_(64993, _a_(64990, _n_(64989, "json", lambda: json), "dumps"), _n_(64991, "data", lambda: data), cls=_n_(64992, "NumpyEncoder", lambda: NumpyEncoder))
_l_(64994)

with _c_(64997, _n_(64995, "open", lambda: open), _n_(64996, "path", lambda: path), 'w') as f:
    _l_(65004)

    _c_(65002, _a_(64999, _n_(64998, "json", lambda: json), "dump"), _n_(65000, "dumped", lambda: dumped), _n_(65001, "f", lambda: f))
    _l_(65003)

