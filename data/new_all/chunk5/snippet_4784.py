# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/48843776/logisticregression-typeerror-not-supported-between-instances-of-str-and
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(694578, _a_(694577, _n_(694576, "df", lambda: df)['Class'], "replace"), 'benign',2, inplace=True)
_l_(694579)
_c_(694582, _a_(694581, _n_(694580, "df", lambda: df)['Class'], "replace"), 'malignant',4, inplace=True)
_l_(694583)
_c_(694586, _a_(694585, _n_(694584, "df", lambda: df), "replace"), '?',10**9,inplace=True)
_l_(694587)
_c_(694593, _a_(694592, _a_(694591, _c_(694590, _a_(694589, _n_(694588, "df", lambda: df), "isnull")), "values"), "any"))#this gives false, data has no missing value
_l_(694594)#this gives false, data has no missing value
X = _c_(694597, _a_(694596, _n_(694595, "df", lambda: df), "drop"), ['Class','Code'], 1)
_l_(694598)
X = _c_(694613, _a_(694608, _c_(694607, _a_(694600, _n_(694599, "pd", lambda: pd), "DataFrame"), {"Constant":_c_(694606, _a_(694602, _n_(694601, "np", lambda: np), "ones"), _c_(694605, _n_(694603, "len", lambda: len), _n_(694604, "X", lambda: X)))}), "join"), _c_(694612, _a_(694610, _n_(694609, "pd", lambda: pd), "DataFrame"), _n_(694611, "X", lambda: X)))
_l_(694614)
y = _n_(694615, "df", lambda: df)['Class']
_l_(694616)
X_train, X_test, y_train, y_test = _c_(694620, _n_(694617, "train_test_split", lambda: train_test_split), _n_(694618, "X", lambda: X), _n_(694619, "y", lambda: y), test_size=0.2, random_state=0)
_l_(694621)
_c_(694625, _a_(694623, _n_(694622, "X_train", lambda: X_train), "astype"), _n_(694624, "int", lambda: int))
_l_(694626)
_c_(694630, _a_(694628, _n_(694627, "y_train", lambda: y_train), "astype"), _n_(694629, "int", lambda: int))
_l_(694631)
X_train = _c_(694635, _a_(694633, _n_(694632, "np", lambda: np), "array"), _n_(694634, "X_train", lambda: X_train))
_l_(694636)
y_train = _c_(694640, _a_(694638, _n_(694637, "np", lambda: np), "array"), _n_(694639, "y_train", lambda: y_train))
_l_(694641)