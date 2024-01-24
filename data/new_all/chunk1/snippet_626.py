# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50678620/typeerror-input-b-of-matmul-op-has-type-float32-that-does-not-match-type-in
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tensorflow as tf
    _l_(386776)

except ImportError:
    pass
try:
    import numpy as np
    _l_(386778)

except ImportError:
    pass

x = ([[3, 4, 5], [1, 2, 3], [3, 2, 5]])
_l_(386779)
y = ([[1, 2, 3, 4, 5, 6, 7, 8], [5, 3, 2, 5, 2, 6, 2, 5], [3, 2, 2, 5, 2, 4, 2, 7]])
_l_(386780)

_c_(386786, _a_(386782, _n_(386781, "tf", lambda: tf), "cast"), _n_(386783, "x", lambda: x), _a_(386785, _n_(386784, "tf", lambda: tf), "float32"))
_l_(386787)
_c_(386793, _a_(386789, _n_(386788, "tf", lambda: tf), "cast"), _n_(386790, "y", lambda: y), _a_(386792, _n_(386791, "tf", lambda: tf), "float32"))
_l_(386794)

train_x = _c_(386798, _a_(386796, _n_(386795, "np", lambda: np), "asarray"), [3.3, 4.4, 5.5, 6.71, 6.93, 4.168, 9.779, 6.182, 7.59, 2.167,
    7.042, 10.791, 5.313, 7.997, 5.654, 9.27, 3.1], dtype=_n_(386797, "float", lambda: float))
_l_(386799)
train_y = _c_(386803, _a_(386801, _n_(386800, "np", lambda: np), "asarray"), [1.7, 2.76, 2.09, 3.19, 1.694, 1.573, 3.366, 2.596, 2.53, 1.221,
    2.827, 3.465, 1.65, 2.904, 2.42, 2.94, 1.3], dtype=_n_(386802, "float", lambda: float))
_l_(386804)

learning_rate = 0.01
_l_(386805)
training_epochs = 100
_l_(386806)
batch_size = 10
_l_(386807)

n_hidden_1 = 256  # number of neurons in first hidden layer
_l_(386808)  # number of neurons in first hidden layer
n_hidden_2 = 256  # ,,      ...      ,,, second hidden layer
_l_(386809)  # ,,      ...      ,,, second hidden layer
n_input = 50  # Dimension of feature used
_l_(386810)  # Dimension of feature used
n_output = 8  # Number of output neurons
_l_(386811)  # Number of output neurons

weights = {
    'hidden_1': _c_(386819, _a_(386813, _n_(386812, "tf", lambda: tf), "Variable"), _c_(386818, _a_(386815, _n_(386814, "tf", lambda: tf), "random_normal"), [_n_(386816, "n_input", lambda: n_input), _n_(386817, "n_hidden_1", lambda: n_hidden_1)])),  # Randomly initialising weights
    'hidden_2': _c_(386827, _a_(386821, _n_(386820, "tf", lambda: tf), "Variable"), _c_(386826, _a_(386823, _n_(386822, "tf", lambda: tf), "random_normal"), [_n_(386824, "n_hidden_1", lambda: n_hidden_1), _n_(386825, "n_hidden_2", lambda: n_hidden_2)])),  # Randomly initialising weights
    'out': _c_(386835, _a_(386829, _n_(386828, "tf", lambda: tf), "Variable"), _c_(386834, _a_(386831, _n_(386830, "tf", lambda: tf), "random_normal"), [_n_(386832, "n_hidden_2", lambda: n_hidden_2), _n_(386833, "n_output", lambda: n_output)]))
}
_l_(386836)
biases = {
    'b1': _c_(386843, _a_(386838, _n_(386837, "tf", lambda: tf), "Variable"), _c_(386842, _a_(386840, _n_(386839, "tf", lambda: tf), "random_normal"), [_n_(386841, "n_hidden_1", lambda: n_hidden_1)])),
    'b2': _c_(386850, _a_(386845, _n_(386844, "tf", lambda: tf), "Variable"), _c_(386849, _a_(386847, _n_(386846, "tf", lambda: tf), "random_normal"), [_n_(386848, "n_hidden_2", lambda: n_hidden_2)])),
    'out': _c_(386857, _a_(386852, _n_(386851, "tf", lambda: tf), "Variable"), _c_(386856, _a_(386854, _n_(386853, "tf", lambda: tf), "random_normal"), [_n_(386855, "n_output", lambda: n_output)]))
}
_l_(386858)


def mlp(_x, _weights, _biases):
    _l_(386899)

    # Defining layers

    layer_1 = _c_(386871, _a_(386861, _a_(386860, _n_(386859, "tf", lambda: tf), "nn"), "relu"), _c_(386870, _a_(386863, _n_(386862, "tf", lambda: tf), "add"), _c_(386868, _a_(386865, _n_(386864, "tf", lambda: tf), "matmul"), _n_(386866, "_x", lambda: _x), _n_(386867, "_weights", lambda: _weights)['hidden_1']), _n_(386869, "_biases", lambda: _biases)['b1']))
    _l_(386872)
    # Choose appropriate activation here
    layer_2 = _c_(386885, _a_(386875, _a_(386874, _n_(386873, "tf", lambda: tf), "nn"), "relu"), _c_(386884, _a_(386877, _n_(386876, "tf", lambda: tf), "add"), _c_(386882, _a_(386879, _n_(386878, "tf", lambda: tf), "matmul"), _n_(386880, "layer_1", lambda: layer_1), _n_(386881, "_weights", lambda: _weights)['hidden_2']), _n_(386883, "_biases", lambda: _biases)['b2']))
    _l_(386886)
    # layer_2 = tf.nn.relu()

    # Linear activation for output
    out_layer = _c_(386895, _a_(386888, _n_(386887, "tf", lambda: tf), "add"), _c_(386893, _a_(386890, _n_(386889, "tf", lambda: tf), "matmul"), _n_(386891, "layer_2", lambda: layer_2), _n_(386892, "_weights", lambda: _weights)['out']), _n_(386894, "_biases", lambda: _biases)['out'])
    _l_(386896)
    aux = _n_(386897, "out_layer", lambda: out_layer)
    _l_(386898)
    return aux


prediction = _c_(386904, _n_(386900, "mlp", lambda: mlp), _n_(386901, "x", lambda: x), _n_(386902, "weights", lambda: weights), _n_(386903, "biases", lambda: biases))
_l_(386905)