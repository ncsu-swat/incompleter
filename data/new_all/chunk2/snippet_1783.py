# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56054091/typeerror-predict-got-an-unexpected-keyword-argument-callbacks
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import keras.callbacks
    _l_(431065)

except ImportError:
    pass
try:
    from keras.models import load_model
    _l_(431067)

except ImportError:
    pass

model = _c_(431070, _n_(431068, "load_model", lambda: load_model), _n_(431069, "strPath_model", lambda: strPath_model))
_l_(431071)
tb_test = _c_(431075, _a_(431073, _a_(431072, keras, "callbacks"), "TensorBoard"), log_dir=_n_(431074, "strPath_model_test_logs", lambda: strPath_model_test_logs),histogram_freq=0, write_graph=True, write_images=True)
_l_(431076)

y_test = _c_(431081, _a_(431078, _n_(431077, "model", lambda: model), "predict"), _n_(431079, "test_val_X", lambda: test_val_X), verbose=1, callbacks=[_n_(431080, "tb_test", lambda: tb_test)])
_l_(431082)