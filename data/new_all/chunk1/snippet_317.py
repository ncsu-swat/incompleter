# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51348085/keras-tutorial-error-nameerror-name-layers-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tensorflow as tf
    _l_(411752)

except ImportError:
    pass
try:
    from tensorflow import keras
    _l_(411754)

except ImportError:
    pass

model = _c_(411757, _a_(411756, _n_(411755, "keras", lambda: keras), "Sequential"))
_l_(411758)
# Adds a densely-connected layer with 64 units to the model:
_c_(411765, _a_(411760, _n_(411759, "model", lambda: model), "add"), _c_(411764, _a_(411763, _a_(411762, _n_(411761, "keras", lambda: keras), "layers"), "Dense"), 64, activation='relu'))
_l_(411766)
# Add another:
_c_(411773, _a_(411768, _n_(411767, "model", lambda: model), "add"), _c_(411772, _a_(411771, _a_(411770, _n_(411769, "keras", lambda: keras), "layers"), "Dense"), 64, activation='relu'))
_l_(411774)
# Add a softmax layer with 10 output units:
_c_(411781, _a_(411776, _n_(411775, "model", lambda: model), "add"), _c_(411780, _a_(411779, _a_(411778, _n_(411777, "keras", lambda: keras), "layers"), "Dense"), 10, activation='softmax'))
_l_(411782)

# Create a sigmoid layer:
_c_(411785, _a_(411784, _n_(411783, "layers", lambda: layers), "Dense"), 64, activation='sigmoid')
_l_(411786)

# A linear layer with L1 regularization of factor 0.01 applied to the kernel matrix:
_c_(411793, _a_(411788, _n_(411787, "layers", lambda: layers), "Dense"), 64, kernel_regularizer=_c_(411792, _a_(411791, _a_(411790, _n_(411789, "keras", lambda: keras), "regularizers"), "l1"), 0.01))
_l_(411794)
# A linear layer with L2 regularization of factor 0.01 applied to the bias vector:
_c_(411801, _a_(411796, _n_(411795, "layers", lambda: layers), "Dense"), 64, bias_regularizer=_c_(411800, _a_(411799, _a_(411798, _n_(411797, "keras", lambda: keras), "regularizers"), "l2"), 0.01))
_l_(411802)

# A linear layer with a kernel initialized to a random orthogonal matrix:
_c_(411805, _a_(411804, _n_(411803, "layers", lambda: layers), "Dense"), 64, kernel_initializer='orthogonal')
_l_(411806)