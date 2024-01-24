# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69209908/tensorflow-typeerror-generator-object-is-not-callable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
data=_c_(421595, _a_(421594, _n_(421593, "pd", lambda: pd), "read_csv"), './test_x_data_OOP3.csv', index_col=[0])
_l_(421596)
data=_c_(421600, _a_(421598, _n_(421597, "np", lambda: np), "array"), _n_(421599, "data", lambda: data))
_l_(421601)
data=_c_(421604, _n_(421602, "reshape_for_Lstm", lambda: reshape_for_Lstm), _n_(421603, "data", lambda: data))  #a function that just transforms the array
_l_(421605)  #a function that just transforms the array