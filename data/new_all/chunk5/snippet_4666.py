# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/52114917/tensorflow-attributeerror-when-a-function-is-passed-to-another
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
input_X = _c_(693824, _a_(693823, _n_(693822, "tf", lambda: tf), "placeholder"), 'float32', [None,64])
_l_(693825)
input_y = _c_(693829, _a_(693827, _n_(693826, "tf", lambda: tf), "placeholder"), 'float32', [None,_n_(693828, "num_classes", lambda: num_classes)])
_l_(693830)

predicted_y = _c_(693839, _a_(693832, _n_(693831, "tf", lambda: tf), "sigmoid"), _c_(693837, _a_(693834, _n_(693833, "tf", lambda: tf), "matmul"), _n_(693835, "input_X", lambda: input_X), _n_(693836, "weights", lambda: weights)) + _n_(693838, "b", lambda: b))
_l_(693840)

def binary_logloss(true_y):
    _l_(693867)


    if _n_(693841, "true_y", lambda: true_y) ==1.:
        _l_(693866)

        aux = _c_(693851, _a_(693843, _n_(693842, "tf", lambda: tf), "reduce_mean"), _c_(693850, _a_(693845, _n_(693844, "tf", lambda: tf), "reduce_sum"), -_c_(693849, _a_(693847, _n_(693846, "tf", lambda: tf), "log"), _n_(693848, "predicted_y", lambda: predicted_y)) , axis=1))
        _l_(693852)
        return aux
    elif _n_(693853, "true_y", lambda: true_y) == 0.:
        _l_(693865)

        aux = _c_(693863, _a_(693855, _n_(693854, "tf", lambda: tf), "reduce_mean"), _c_(693862, _a_(693857, _n_(693856, "tf", lambda: tf), "reduce_sum"), -_c_(693861, _a_(693859, _n_(693858, "tf", lambda: tf), "log"), 1-_n_(693860, "predicted_y", lambda: predicted_y)) , axis=1))
        _l_(693864)
        return aux

def train_function(X, y):
    _l_(693893)

    loss = _c_(693870, _n_(693868, "binary_logloss", lambda: binary_logloss), _n_(693869, "input_y", lambda: input_y))
    _l_(693871)
    optimizer = _c_(693878, _a_(693876, _c_(693875, _a_(693874, _a_(693873, _n_(693872, "tf", lambda: tf), "train"), "GradientDescentOptimizer"), 0.001), "minimize"), _n_(693877, "loss", lambda: loss))
    _l_(693879)
    _, c = _c_(693888, _a_(693881, _n_(693880, "s", lambda: s), "run"), [_n_(693882, "optimizer", lambda: optimizer), _n_(693883, "loss", lambda: loss)], {_n_(693884, "input_X", lambda: input_X):_n_(693885, "X", lambda: X), _n_(693886, "input_y", lambda: input_y):_n_(693887, "y", lambda: y)})
    _l_(693889)
    aux = _n_(693890, "_", lambda: _), _n_(693891, "c", lambda: c)
    _l_(693892)
    return aux

_c_(693899, _a_(693895, _n_(693894, "s", lambda: s), "run"), _c_(693898, _a_(693897, _n_(693896, "tf", lambda: tf), "global_variables_initializer")))
_l_(693900)
for epoch in _n_(693901, "epochs", lambda: epochs):
    _l_(693907)

    _, c = _c_(693905, _n_(693902, "train_function", lambda: train_function), _n_(693903, "batch_x_train", lambda: batch_x_train), _n_(693904, "batch_y_train", lambda: batch_y_train)) 
    _l_(693906) 