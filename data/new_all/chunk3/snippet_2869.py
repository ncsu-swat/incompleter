# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60394722/why-does-it-say-this-typeerror-call-missing-1-required-positional-argum
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from keras.models import Sequential
    _l_(531637)

except ImportError:
    pass
try:
    from keras.layers import Dense, Conv2D, MaxPooling2D, Dropout
    _l_(531639)

except ImportError:
    pass
try:
    from keras.layers import Flatten, Activation
    _l_(531641)

except ImportError:
    pass
try:
    from keras.applications.vgg16 import VGG16
    _l_(531643)

except ImportError:
    pass
try:
    from keras.models import Model
    _l_(531645)

except ImportError:
    pass
try:
    from keras import backend as K
    _l_(531647)

except ImportError:
    pass

def swish(x):
    _l_(531654)

    aux = _c_(531651, _a_(531649, _n_(531648, "K", lambda: K), "sigmoid"), _n_(531650, "x", lambda: x)) * _n_(531652, "x", lambda: x)
    _l_(531653)
    return aux

custom_vgg = _c_(531656, _n_(531655, "Sequential", lambda: Sequential))
_l_(531657)
img_width = 224
_l_(531658)
img_height = 224
_l_(531659)
vgg_model = _c_(531663, _n_(531660, "VGG16", lambda: VGG16), include_top=False, weights='imagenet',input_shape=(_n_(531661, "img_width", lambda: img_width), _n_(531662, "img_height", lambda: img_height), 3))
_l_(531664)
_c_(531669, _n_(531665, "print", lambda: print), _c_(531668, _a_(531667, _n_(531666, "vgg_model", lambda: vgg_model), "get_config")))
_l_(531670)
#vgg_model.save_weights('models/vgg_weights.h5')
for layer in _a_(531672, _n_(531671, "vgg_model", lambda: vgg_model), "layers"):
    _l_(531697)

    if _a_(531675, _a_(531674, _n_(531673, "layer", lambda: layer), "__class__"), "__name__")=='MaxPooling2D':
        _l_(531696)

        _n_(531676, "layer", lambda: layer).trainable = False
        _l_(531677)
        _c_(531683, _a_(531679, _n_(531678, "custom_vgg", lambda: custom_vgg), "add"), _c_(531682, _n_(531680, "layer", lambda: layer), activation = _n_(531681, "swish", lambda: swish)))
        _l_(531684)
        _c_(531689, _a_(531686, _n_(531685, "custom_vgg", lambda: custom_vgg), "add"), _c_(531688, _n_(531687, "Dropout", lambda: Dropout), 0.4))
        _l_(531690)
    else :
        _c_(531694, _a_(531692, _n_(531691, "custom_vgg", lambda: custom_vgg), "add"), _n_(531693, "layer", lambda: layer))
        _l_(531695)
_c_(531702, _a_(531699, _n_(531698, "custom_vgg", lambda: custom_vgg), "add"), _c_(531701, _n_(531700, "Flatten", lambda: Flatten)))
_l_(531703)
_c_(531709, _a_(531705, _n_(531704, "custom_vgg", lambda: custom_vgg), "add"), _c_(531708, _n_(531706, "Dense", lambda: Dense), 1024,activation=_n_(531707, "swish", lambda: swish)))
_l_(531710)
_c_(531716, _a_(531712, _n_(531711, "custom_vgg", lambda: custom_vgg), "add"), _c_(531715, _n_(531713, "Dense", lambda: Dense), 1024,activation=_n_(531714, "swish", lambda: swish)))
_l_(531717)
_c_(531722, _a_(531719, _n_(531718, "custom_vgg", lambda: custom_vgg), "add"), _c_(531721, _n_(531720, "Dense", lambda: Dense), 128, activation = "softmax"))
_l_(531723)

_c_(531726, _a_(531725, _n_(531724, "custom_vgg", lambda: custom_vgg), "compile"), optimizer = "adam", loss = "categorical_crossentropy", metrics = ["accuracy"])
_l_(531727)

_c_(531730, _a_(531729, _n_(531728, "custom_vgg", lambda: custom_vgg), "summary")) 
_l_(531731) 