# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64654126/numpy-typeerror-must-be-integer-not-tuple
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(421418)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(421420)

except ImportError:
    pass


def load_data(path):
    _l_(421447)

    datum= []
    _l_(421421)
    with _c_(421424, _n_(421422, "open", lambda: open), _n_(421423, "path", lambda: path)) as fp:
        _l_(421444)

        line = _c_(421427, _a_(421426, _n_(421425, "fp", lambda: fp), "readline"))
        _l_(421428)
        while _n_(421429, "line", lambda: line):
            _l_(421443)

            arr_line= _c_(421432, _a_(421431, _n_(421430, "line", lambda: line), "split"), ",")
            _l_(421433)
            _c_(421437, _a_(421435, _n_(421434, "datum", lambda: datum), "append"), _n_(421436, "arr_line", lambda: arr_line))
            _l_(421438)
            line=_c_(421441, _a_(421440, _n_(421439, "fp", lambda: fp), "readline"))
            _l_(421442)
    aux = _n_(421445, "datum", lambda: datum)
    _l_(421446)
    return aux

#Sigmoid function
def sigmoid(x):
    _l_(421453)

    aux = 1/(1+_c_(421451, _a_(421449, _n_(421448, "np", lambda: np), "exp"), -_n_(421450, "x", lambda: x)))
    _l_(421452)
    return aux

#Loss function
def square_loss(y_pred, target):
    _l_(421462)

    aux = _c_(421460, _a_(421455, _n_(421454, "np", lambda: np), "mean"), _c_(421459, _n_(421456, "pow", lambda: pow), ((_n_(421457, "y_pred", lambda: y_pred) - _n_(421458, "target", lambda: target)),2)))
    _l_(421461)
    return aux

if _n_(421463, "__name__", lambda: __name__) == "__main__":
    _l_(421488)

    # load the data from the file
    matrix_data = _c_(421465, _n_(421464, "load_data", lambda: load_data), "all_data.txt")
    _l_(421466)
    _c_(421470, _a_(421468, _n_(421467, "np", lambda: np), "array"), _n_(421469, "matrix_data", lambda: matrix_data))
    _l_(421471)

    _c_(421476, _a_(421474, _a_(421473, _n_(421472, "np", lambda: np), "random"), "shuffle"), _n_(421475, "matrix_data", lambda: matrix_data))
    _l_(421477)

    training_data = _n_(421478, "matrix_data", lambda: matrix_data)[167:,:] #These all lines gives error
    _l_(421479) #These all lines gives error
    test_data = _n_(421480, "matrix_data", lambda: matrix_data)[41:,:] #These all lines gives error
    _l_(421481) #These all lines gives error

    X_tr, y_tr = _n_(421482, "training_data", lambda: training_data)[:, :-1], _n_(421483, "training_data", lambda: training_data)[:, -1] #These all lines gives error
    _l_(421484) #These all lines gives error
    X_te, y_te = _n_(421485, "test_data", lambda: test_data)[:, :-1], _n_(421486, "test_data", lambda: test_data)[:, -1] #These all lines gives error
    _l_(421487) #These all lines gives error