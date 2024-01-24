# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54064897/attributeerror-nonetype-object-has-no-attribute-image-data-format-in-keras
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from keras import backend as K
    _l_(451086)

except ImportError:
    pass
try:
    from keras_applications.resnet50 import ResNet50
    _l_(451088)

except ImportError:
    pass
try:
    from keras.layers import Input
    _l_(451090)

except ImportError:
    pass
try:
    from keras.callbacks import ModelCheckpoint
    _l_(451092)

except ImportError:
    pass

_c_(451095, _a_(451094, _n_(451093, "K", lambda: K), "set_image_data_format"), 'channels_last')
_l_(451096)
_c_(451099, _a_(451098, _n_(451097, "K", lambda: K), "set_image_dim_ordering"), 'tf')
_l_(451100)

input_layer = _c_(451102, _n_(451101, "Input", lambda: Input), shape=(224, 224, 3))
_l_(451103)
model = _c_(451105, _n_(451104, "ResNet50", lambda: ResNet50), include_top=True, weights=None, classes=2)
_l_(451106)
_c_(451109, _a_(451108, _n_(451107, "model", lambda: model), "compile"), optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])
_l_(451110)