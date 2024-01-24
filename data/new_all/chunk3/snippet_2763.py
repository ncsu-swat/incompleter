# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64058523/attributeerror-sequential-object-has-no-attribute-make-predict-function
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tensorflow.keras.models import model_from_json
    _l_(552711)

except ImportError:
    pass
try:
    import numpy as np
    _l_(552713)

except ImportError:
    pass
try:
    import tensorflow as tf
    _l_(552715)

except ImportError:
    pass

config = _c_(552720, _a_(552719, _a_(552718, _a_(552717, _n_(552716, "tf", lambda: tf), "compat"), "v1"), "ConfigProto"))
_l_(552721)

_a_(552723, _n_(552722, "config", lambda: config), "gpu_options").per_process_gpu_memory_fraction = 0.15
_l_(552724)

session = _c_(552730, _a_(552728, _a_(552727, _a_(552726, _n_(552725, "tf", lambda: tf), "compat"), "v1"), "Session"), config=_n_(552729, "config", lambda: config))
_l_(552731)


class FacialExpressionModel(_n_(552732, "object", lambda: object)):
    _l_(552775)


    EMOTIONS_LIST = ["Angry", "Disgust",
                     "Fear", "Happy",
                     "Neutral", "Sad",
                     "Surprise"]
    _l_(552733)

    def __init__(self, model_json_file, model_weights_file):
        _l_(552758)

        # load model from JSON file
        with _c_(552736, _n_(552734, "open", lambda: open), _n_(552735, "model_json_file", lambda: model_json_file), "r") as json_file:
            _l_(552746)

            loaded_model_json = _c_(552739, _a_(552738, _n_(552737, "json_file", lambda: json_file), "read"))
            _l_(552740)
            _n_(552741, "self", lambda: self).loaded_model = _c_(552744, _n_(552742, "model_from_json", lambda: model_from_json), _n_(552743, "loaded_model_json", lambda: loaded_model_json))
            _l_(552745)

        # load weights into the new model
        _c_(552751, _a_(552749, _a_(552748, _n_(552747, "self", lambda: self), "loaded_model"), "load_weights"), _n_(552750, "model_weights_file", lambda: model_weights_file))
        _l_(552752)
        _c_(552756, _a_(552755, _a_(552754, _n_(552753, "self", lambda: self), "loaded_model"), "_make_predict_function"))
        _l_(552757)

    def predict_emotion(self, img):
        _l_(552774)

        _n_(552759, "self", lambda: self).preds = _c_(552764, _a_(552762, _a_(552761, _n_(552760, "self", lambda: self), "loaded_model"), "predict"), _n_(552763, "img", lambda: img))
        _l_(552765)
        aux = _a_(552767, _n_(552766, "FacialExpressionModel", lambda: FacialExpressionModel), "EMOTIONS_LIST")[_c_(552772, _a_(552769, _n_(552768, "np", lambda: np), "argmax"), _a_(552771, _n_(552770, "self", lambda: self), "preds"))]
        _l_(552773)
        return aux