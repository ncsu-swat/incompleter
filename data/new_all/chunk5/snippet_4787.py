# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/48843776/logisticregression-typeerror-not-supported-between-instances-of-str-and
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(664361, _a_(664360, _n_(664359, "df", lambda: df)['Class'], "replace"), 'benign',2, inplace=True)
_l_(664362)
_c_(664365, _a_(664364, _n_(664363, "df", lambda: df)['Class'], "replace"), 'malignant',4, inplace=True)
_l_(664366)
_c_(664369, _a_(664368, _n_(664367, "df", lambda: df), "replace"), '?',10**9,inplace=True)
_l_(664370)
_c_(664376, _a_(664375, _a_(664374, _c_(664373, _a_(664372, _n_(664371, "df", lambda: df), "isnull")), "values"), "any"))#this gives false, data has no missing value
_l_(664377)#this gives false, data has no missing value
X = _c_(664380, _a_(664379, _n_(664378, "df", lambda: df), "drop"), ['Class','Code'], 1)
_l_(664381)
X = _c_(664396, _a_(664391, _c_(664390, _a_(664383, _n_(664382, "pd", lambda: pd), "DataFrame"), {"Constant":_c_(664389, _a_(664385, _n_(664384, "np", lambda: np), "ones"), _c_(664388, _n_(664386, "len", lambda: len), _n_(664387, "X", lambda: X)))}), "join"), _c_(664395, _a_(664393, _n_(664392, "pd", lambda: pd), "DataFrame"), _n_(664394, "X", lambda: X)))
_l_(664397)
y = _n_(664398, "df", lambda: df)['Class']
_l_(664399)
X_train, X_test, y_train, y_test = _c_(664403, _n_(664400, "train_test_split", lambda: train_test_split), _n_(664401, "X", lambda: X), _n_(664402, "y", lambda: y), test_size=0.2, random_state=0)
_l_(664404)
_c_(664408, _a_(664406, _n_(664405, "X_train", lambda: X_train), "astype"), _n_(664407, "int", lambda: int))
_l_(664409)
_c_(664413, _a_(664411, _n_(664410, "y_train", lambda: y_train), "astype"), _n_(664412, "int", lambda: int))
_l_(664414)
X_train = _c_(664418, _a_(664416, _n_(664415, "np", lambda: np), "array"), _n_(664417, "X_train", lambda: X_train))
_l_(664419)
y_train = _c_(664423, _a_(664421, _n_(664420, "np", lambda: np), "array"), _n_(664422, "y_train", lambda: y_train))
_l_(664424)