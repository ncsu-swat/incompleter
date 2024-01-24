# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67420828/pandas-typeerror-when-using-cudf-dataframe-but-not-pandas
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import cudf
    _l_(432357)

except ImportError:
    pass
try:
    from cuml.model_selection import train_test_split
    _l_(432359)

except ImportError:
    pass

dataTest = _c_(432363, _a_(432361, _n_(432360, "cudf", lambda: cudf), "read_csv"), _n_(432362, "MY_DATA", lambda: MY_DATA))
_l_(432364)

X = _a_(432366, _n_(432365, "dataTest", lambda: dataTest), "iloc")[:, [1,12]]
_l_(432367)
y = _a_(432369, _n_(432368, "dataTest", lambda: dataTest), "iloc")[:,12]
_l_(432370)

X_train, X_test, y_train, y_test = _c_(432374, _n_(432371, "train_test_split", lambda: train_test_split), _n_(432372, "X", lambda: X), _n_(432373, "y", lambda: y), train_size=.2, random_state=610)
_l_(432375)