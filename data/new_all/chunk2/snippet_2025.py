# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68776470/typeerror-preprocess-input-got-an-unexpected-keyword-argument-mode
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from keras.applications.vgg16 import preprocess_input
    _l_(428075)

except ImportError:
    pass
X = _c_(428078, _n_(428076, "preprocess_input", lambda: preprocess_input), _n_(428077, "X", lambda: X), mode='tf')  
_l_(428079)  