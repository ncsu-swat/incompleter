# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70836134/mlp-regression-error-typeerror-not-supported-between-instances-of-numpy
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
mlp = _c_(634913, _n_(634912, "MLPRegressor", lambda: MLPRegressor))
_l_(634914)
parameter_space = {
    'max_iter': [1000,2000,5000],
    'activation': ['relu'],
    'alpha': [0.0001,0.001,0.01],
    'hidden_layer_sizes': [(8,8,),(50,50,),(100,100,)],
    'solver': ['sgd', 'adam'],
    'learning_rate': ['constant','adaptive']
}
_l_(634915)
k = 5
_l_(634916)
kf = _c_(634919, _n_(634917, "KFold", lambda: KFold), n_splits=_n_(634918, "k", lambda: k), random_state=None)
_l_(634920)
model = _c_(634923, _n_(634921, "MLPRegressor", lambda: MLPRegressor), _n_(634922, "parameter_space", lambda: parameter_space))
_l_(634924)
acc_score = []
_l_(634925)
for train_index , test_index in _c_(634929, _a_(634927, _n_(634926, "kf", lambda: kf), "split"), _n_(634928, "x", lambda: x)):
    _l_(634946)

    x_train , x_valid = _n_(634930, "x", lambda: x)[_n_(634931, "train_index", lambda: train_index),:],_n_(634932, "x", lambda: x)[_n_(634933, "test_index", lambda: test_index),:]
    _l_(634934)
    y_train , y_valid = _n_(634935, "y", lambda: y)[_n_(634936, "train_index", lambda: train_index)] , _n_(634937, "y", lambda: y)[_n_(634938, "test_index", lambda: test_index)]
    _l_(634939)
    _c_(634944, _a_(634941, _n_(634940, "model", lambda: model), "fit"), _n_(634942, "x_train", lambda: x_train)[1:50], _n_(634943, "y_train", lambda: y_train)[1:50])
    _l_(634945)