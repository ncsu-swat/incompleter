# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/52114917/tensorflow-attributeerror-when-a-function-is-passed-to-another
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
input_X = _c_(656019, _a_(656018, _n_(656017, "tf", lambda: tf), "placeholder"), 'float32', [None,64])
_l_(656020)
input_y = _c_(656024, _a_(656022, _n_(656021, "tf", lambda: tf), "placeholder"), 'float32', [None,_n_(656023, "num_classes", lambda: num_classes)])
_l_(656025)

predicted_y = _c_(656034, _a_(656027, _n_(656026, "tf", lambda: tf), "sigmoid"), _c_(656032, _a_(656029, _n_(656028, "tf", lambda: tf), "matmul"), _n_(656030, "input_X", lambda: input_X), _n_(656031, "weights", lambda: weights)) + _n_(656033, "b", lambda: b))
_l_(656035)

def binary_logloss(true_y):
    _l_(656062)


    if _n_(656036, "true_y", lambda: true_y) ==1.:
        _l_(656061)

        aux = _c_(656046, _a_(656038, _n_(656037, "tf", lambda: tf), "reduce_mean"), _c_(656045, _a_(656040, _n_(656039, "tf", lambda: tf), "reduce_sum"), -_c_(656044, _a_(656042, _n_(656041, "tf", lambda: tf), "log"), _n_(656043, "predicted_y", lambda: predicted_y)) , axis=1))
        _l_(656047)
        return aux
    elif _n_(656048, "true_y", lambda: true_y) == 0.:
        _l_(656060)

        aux = _c_(656058, _a_(656050, _n_(656049, "tf", lambda: tf), "reduce_mean"), _c_(656057, _a_(656052, _n_(656051, "tf", lambda: tf), "reduce_sum"), -_c_(656056, _a_(656054, _n_(656053, "tf", lambda: tf), "log"), 1-_n_(656055, "predicted_y", lambda: predicted_y)) , axis=1))
        _l_(656059)
        return aux

def train_function(X, y):
    _l_(656088)

    loss = _c_(656065, _n_(656063, "binary_logloss", lambda: binary_logloss), _n_(656064, "input_y", lambda: input_y))
    _l_(656066)
    optimizer = _c_(656073, _a_(656071, _c_(656070, _a_(656069, _a_(656068, _n_(656067, "tf", lambda: tf), "train"), "GradientDescentOptimizer"), 0.001), "minimize"), _n_(656072, "loss", lambda: loss))
    _l_(656074)
    _, c = _c_(656083, _a_(656076, _n_(656075, "s", lambda: s), "run"), [_n_(656077, "optimizer", lambda: optimizer), _n_(656078, "loss", lambda: loss)], {_n_(656079, "input_X", lambda: input_X):_n_(656080, "X", lambda: X), _n_(656081, "input_y", lambda: input_y):_n_(656082, "y", lambda: y)})
    _l_(656084)
    aux = _n_(656085, "_", lambda: _), _n_(656086, "c", lambda: c)
    _l_(656087)
    return aux

_c_(656094, _a_(656090, _n_(656089, "s", lambda: s), "run"), _c_(656093, _a_(656092, _n_(656091, "tf", lambda: tf), "global_variables_initializer")))
_l_(656095)
for epoch in _n_(656096, "epochs", lambda: epochs):
    _l_(656102)

    _, c = _c_(656100, _n_(656097, "train_function", lambda: train_function), _n_(656098, "batch_x_train", lambda: batch_x_train), _n_(656099, "batch_y_train", lambda: batch_y_train)) 
    _l_(656101) 