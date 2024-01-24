# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65529910/nameerror-name-predicted-is-not-defined-while-using-google-colab
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from google.colab import drive
    _l_(556890)

except ImportError:
    pass

_c_(556893, _a_(556892, _n_(556891, "drive", lambda: drive), "mount"), '/content/drive')
_l_(556894)
try:
    import numpy as np
    _l_(556896)

except ImportError:
    pass
try:
    from sklearn import datasets
    _l_(556898)

except ImportError:
    pass
try:
    from sklearn.model_selection import train_test_split
    _l_(556900)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(556902)

except ImportError:
    pass
try:
    from matplotlib.colors import ListedColormap
    _l_(556904)

except ImportError:
    pass
cmap = _c_(556906, _n_(556905, "ListedColormap", lambda: ListedColormap), ['#FF0000', '#00FF00', '#0000FF'])
_l_(556907)

iris = _c_(556910, _a_(556909, _n_(556908, "datasets", lambda: datasets), "load_iris"))
_l_(556911)
X, y = _a_(556913, _n_(556912, "iris", lambda: iris), "data"), _a_(556915, _n_(556914, "iris", lambda: iris), "target")
_l_(556916)

X_train, X_test, y_train, y_test = _c_(556920, _n_(556917, "train_test_split", lambda: train_test_split), _n_(556918, "X", lambda: X), _n_(556919, "y", lambda: y), test_size = 0.2, random_state = 1234)
_l_(556921)
try:
    import sys
    _l_(556923)

except ImportError:
    pass
_c_(556927, _a_(556926, _a_(556925, _n_(556924, "sys", lambda: sys), "path"), "append"), '/content/drive/MyDrive/Colab Notebooks')
_l_(556928)
try:
    from knn import KNN
    _l_(556930)

except ImportError:
    pass
clf = _c_(556932, _n_(556931, "KNN", lambda: KNN), k=3)
_l_(556933)
_c_(556938, _a_(556935, _n_(556934, "clf", lambda: clf), "fit"), _n_(556936, "X_train", lambda: X_train), _n_(556937, "y_train", lambda: y_train))
_l_(556939)
predictions = _c_(556943, _a_(556941, _n_(556940, "clf", lambda: clf), "predict"), _n_(556942, "X_test", lambda: X_test))
_l_(556944)
acc = _c_(556949, _a_(556946, _n_(556945, "np", lambda: np), "sum"), _n_(556947, "predictions", lambda: predictions) == _n_(556948, "y_test", lambda: y_test)) / _c_(556952, _n_(556950, "len", lambda: len), _n_(556951, "y_test", lambda: y_test))
_l_(556953)
_c_(556956, _n_(556954, "print", lambda: print), _n_(556955, "acc", lambda: acc))
_l_(556957)