# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/46732047/typeerror-for-predict-probanp-arraytest
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
model = _c_(440184, _n_(440183, "LogisticRegression", lambda: LogisticRegression))
_l_(440185)
model = _c_(440190, _a_(440187, _n_(440186, "model", lambda: model), "fit"), _n_(440188, "X", lambda: X), _n_(440189, "y", lambda: y))
_l_(440191)
test_data = [1,2,3,4,5,6,7,8,9,10,11,12,13]
_l_(440192)
test_prediction = _c_(440199, _a_(440194, _n_(440193, "model", lambda: model), "predict_proba"), _c_(440198, _a_(440196, _n_(440195, "np", lambda: np), "array"), _n_(440197, "test_data", lambda: test_data)))
_l_(440200)
max = -1.0
_l_(440201)
res = 0
_l_(440202)
for i in _c_(440205, _n_(440203, "range", lambda: range), _n_(440204, "test_prediction", lambda: test_prediction)):
    _l_(440215)

    if _n_(440206, "test_prediction", lambda: test_prediction)[_n_(440207, "i", lambda: i)]>_n_(440208, "max", lambda: max):
        _l_(440214)

        max = _n_(440209, "test_prediction", lambda: test_prediction)[_n_(440210, "i", lambda: i)]
        _l_(440211)
        res = _n_(440212, "i", lambda: i)
        _l_(440213)
if _n_(440216, "res", lambda: res)==0:
    _l_(440228)

    _c_(440218, _n_(440217, "print", lambda: print), 'A')
    _l_(440219)
elif _n_(440220, "res", lambda: res)==1:
    _l_(440227)

    _c_(440222, _n_(440221, "print", lambda: print), 'B')
    _l_(440223)
else:
    _c_(440225, _n_(440224, "print", lambda: print), 'C')
    _l_(440226)