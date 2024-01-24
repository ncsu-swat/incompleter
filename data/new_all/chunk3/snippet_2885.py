# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59834367/numpy-array-typeerror-dataframe-object-is-not-callable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(534900)

except ImportError:
    pass
try:
    import numpy as np
    _l_(534902)

except ImportError:
    pass
try:
    import sklearn
    _l_(534904)

except ImportError:
    pass
try:
    from sklearn import linear_model
    _l_(534906)

except ImportError:
    pass
try:
    from sklearn.utils import shuffle
    _l_(534908)

except ImportError:
    pass

data = _c_(534911, _a_(534910, _n_(534909, "pd", lambda: pd), "read_csv"), "student-mat.csv", sep=";")
_l_(534912)

_c_(534914, _n_(534913, "print", lambda: print), "Starting data manipulation...")
_l_(534915)
data = _n_(534916, "data", lambda: data)[["G1", "G2", "G3", "studytime", "failures", "absences"]]
_l_(534917)

predict = "G3"
_l_(534918)

x = _c_(534925, _a_(534920, _n_(534919, "np", lambda: np), "array"), _c_(534924, _a_(534922, _n_(534921, "data", lambda: data), "drop"), [_n_(534923, "predict", lambda: predict)], 1))
_l_(534926)
y = _c_(534932, _a_(534928, _n_(534927, "np", lambda: np), "array"), _c_(534931, _n_(534929, "data", lambda: data), [_n_(534930, "predict", lambda: predict)]))
_l_(534933)


x_train, x_test, y_train, y_test = _c_(534939, _a_(534936, _a_(534935, _n_(534934, "sklearn", lambda: sklearn), "model_selection"), "train_test_split"), _n_(534937, "x", lambda: x), _n_(534938, "y", lambda: y), test_size=0.1)
_l_(534940)

linear = _c_(534943, _a_(534942, _n_(534941, "linear_model", lambda: linear_model), "LinearRegression"))
_l_(534944)
_c_(534949, _a_(534946, _n_(534945, "linear", lambda: linear), "fit"), _n_(534947, "x_train", lambda: x_train), _n_(534948, "y_train", lambda: y_train))
_l_(534950)
acc = _c_(534955, _a_(534952, _n_(534951, "linear", lambda: linear), "score"), _n_(534953, "x_test", lambda: x_test), _n_(534954, "y_test", lambda: y_test))
_l_(534956)

_c_(534961, _n_(534957, "print", lambda: print), "Accuracy: " + _c_(534960, _n_(534958, "str", lambda: str), _n_(534959, "acc", lambda: acc)))
_l_(534962)

_c_(534968, _n_(534963, "print", lambda: print), "Coefficient: " + _c_(534967, _n_(534964, "str", lambda: str), _a_(534966, _n_(534965, "linear", lambda: linear), "coef_")))
_l_(534969)
_c_(534975, _n_(534970, "print", lambda: print), "Intercept: " + _c_(534974, _n_(534971, "str", lambda: str), _a_(534973, _n_(534972, "linear", lambda: linear), "intercept_")))
_l_(534976)