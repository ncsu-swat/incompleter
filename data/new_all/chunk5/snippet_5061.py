# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64168242/error-nameerror-name-self-is-not-defined-even-though-i-declare-self
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class AdaBoost_regressor():
    _l_(658593)

    def __init__(self, n_estimators, functions):
        _l_(658588)

        # n_estimators is the number of weak regressors     
        _n_(658579, "self", lambda: self).n_estimators = _n_(658580, "n_estimators", lambda: n_estimators)
        _l_(658581)
        
        # We will store the sequence of functions in object "functions"
        _n_(658582, "self", lambda: self).functions = _c_(658586, _a_(658584, _n_(658583, "np", lambda: np), "array"), [None] * _n_(658585, "n_estimators", lambda: n_estimators), dtype = 'f')
        _l_(658587)
    
    # We set f_0 = 0
    def f_0(x):
        _l_(658590)

        aux = 0
        _l_(658589)
        return aux
    _a_(658591, self, "functions")[0] = f_0
    _l_(658592)