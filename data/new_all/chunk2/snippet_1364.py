# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69653835/attribute-error-pickle-load-seldon-deployment
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pickle
    _l_(454797)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(454799)

except ImportError:
    pass
try:
    import dill
    _l_(454801)

except ImportError:
    pass
try:
    from MyPipelines.CustomPipelines import MyEncoder
    _l_(454803)

except ImportError:
    pass
try:
    from MyPipelines.CustomPipelines import *
    _l_(454805)

except ImportError:
    pass
try:
    import MyPipelines.CustomPipelines
    _l_(454807)

except ImportError:
    pass

class my_prediction:
    _l_(454843)

   
    def __init__(self):
        _l_(454819)


        file_name = 'model.sav'
        _l_(454808)
        with _c_(454811, _n_(454809, "open", lambda: open), _n_(454810, "file_name", lambda: file_name), 'rb') as model_file:
            _l_(454818)

            _n_(454812, "self", lambda: self).model = _c_(454816, _a_(454814, _n_(454813, "pickle", lambda: pickle), "load"), _n_(454815, "model_file", lambda: model_file))
            _l_(454817)

    def predict(self, request):
        _l_(454842)

        data = _c_(454822, _a_(454821, _n_(454820, "request", lambda: request), "get"), 'ndarray')
        _l_(454823)
        columns = _c_(454826, _a_(454825, _n_(454824, "request", lambda: request), "get"), 'names')
        _l_(454827)
        X = _c_(454832, _a_(454829, _n_(454828, "pd", lambda: pd), "DataFrame"), _n_(454830, "data", lambda: data), columns = _n_(454831, "columns", lambda: columns))
        _l_(454833)
        predictions = _c_(454838, _a_(454836, _a_(454835, _n_(454834, "self", lambda: self), "model"), "predict"), _n_(454837, "X", lambda: X))
        _l_(454839)
        aux = _n_(454840, "predictions", lambda: predictions)
        _l_(454841)
        return aux