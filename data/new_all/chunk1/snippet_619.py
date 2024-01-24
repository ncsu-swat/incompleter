# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55407970/how-to-fix-typeerror-the-added-layer-must-be-an-instance-of-class-layer-in-p
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import keras
    _l_(384016)

except ImportError:
    pass
try:
    import numpy as np
    _l_(384018)

except ImportError:
    pass
try:
    from sklearn.model_selection import train_test_split
    _l_(384020)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(384022)

except ImportError:
    pass
try:
    from sklearn.utils import shuffle
    _l_(384024)

except ImportError:
    pass
try:
    import tensorflow as tf
    _l_(384026)

except ImportError:
    pass

seed = 10
_l_(384027)
_c_(384032, _a_(384030, _a_(384029, _n_(384028, "np", lambda: np), "random"), "seed"), _n_(384031, "seed", lambda: seed))
_l_(384033)

dataset = _c_(384036, _a_(384035, _n_(384034, "np", lambda: np), "loadtxt"), "dataset2.csv",delimiter=',',skiprows=1)
_l_(384037)
dataset = _c_(384040, _n_(384038, "shuffle", lambda: shuffle), _n_(384039, "dataset", lambda: dataset))
_l_(384041)

X = _n_(384042, "dataset", lambda: dataset)[:,2:]
_l_(384043)
Y = _n_(384044, "dataset", lambda: dataset)[:,1]
_l_(384045)

(X_train,X_test,Y_train,Y_test) = _c_(384050, _n_(384046, "train_test_split", lambda: train_test_split), _n_(384047, "X", lambda: X), _n_(384048, "Y", lambda: Y), test_size=0.15, random_state=_n_(384049, "seed", lambda: seed))
_l_(384051)
input_shape = (13,)
_l_(384052)

model = _c_(384057, _a_(384056, _a_(384055, _a_(384054, _n_(384053, "tf", lambda: tf), "keras"), "models"), "Sequential"))
_l_(384058)
_c_(384066, _a_(384060, _n_(384059, "model", lambda: model), "add"), _c_(384065, _a_(384063, _a_(384062, _n_(384061, "keras", lambda: keras), "layers"), "InputLayer"), _n_(384064, "input_shape", lambda: input_shape)))
_l_(384067)
_c_(384075, _a_(384069, _n_(384068, "model", lambda: model), "add"), _c_(384074, _a_(384073, _a_(384072, _a_(384071, _n_(384070, "keras", lambda: keras), "layers"), "core"), "Dense"), 128, activation='relu'))
_l_(384076)
_c_(384084, _a_(384078, _n_(384077, "model", lambda: model), "add"), _c_(384083, _a_(384082, _a_(384081, _a_(384080, _n_(384079, "keras", lambda: keras), "layers"), "core"), "Dense"), 128, activation='relu'))
_l_(384085)
_c_(384093, _a_(384087, _n_(384086, "model", lambda: model), "add"), _c_(384092, _a_(384091, _a_(384090, _a_(384089, _n_(384088, "keras", lambda: keras), "layers"), "core"), "Dense"), 4, activation='sigmoid'))
_l_(384094)

_c_(384097, _a_(384096, _n_(384095, "model", lambda: model), "compile"), optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
_l_(384098)

_c_(384103, _a_(384100, _n_(384099, "model", lambda: model), "fit"), _n_(384101, "X_train", lambda: X_train),_n_(384102, "Y_train", lambda: Y_train),epochs=20)
_l_(384104)