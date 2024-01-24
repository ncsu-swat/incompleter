# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56090708/why-am-i-getting-attributeerror-linearregressiongd-object-has-no-attribute-n
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class LinearRegressionGD (_n_(427368, "object", lambda: object)):
    _l_(427467)


    def _init_(self, eta=0.001, n_iter=20):
        _l_(427375)

        _n_(427369, "self", lambda: self).eta = _n_(427370, "eta", lambda: eta)
        _l_(427371)
        _n_(427372, "self", lambda: self).n_iter = _n_(427373, "n_iter", lambda: n_iter)
        _l_(427374)

    def fit(self, X, y):
        _l_(427428)

        _n_(427376, "self", lambda: self).w = _c_(427381, _a_(427378, _n_(427377, "np", lambda: np), "zeros"), 1 + _a_(427380, _n_(427379, "X", lambda: X), "shape")[1])
        _l_(427382)
        _n_(427383, "self", lambda: self).cost_ = {}
        _l_(427384)

        for i in _c_(427388, _n_(427385, "range", lambda: range), _a_(427387, _n_(427386, "self", lambda: self), "n_iter")):
            _l_(427425)

            output = _c_(427392, _a_(427390, _n_(427389, "self", lambda: self), "net_input"), _n_(427391, "X", lambda: X))
            _l_(427393)
            errors = (_n_(427394, "y", lambda: y) - _n_(427395, "output", lambda: output))
            _l_(427396)
            _a_(427398, _n_(427397, "self", lambda: self), "w_")[1:] += _a_(427400, _n_(427399, "self", lambda: self), "eta") * _c_(427405, _a_(427403, _a_(427402, _n_(427401, "X", lambda: X), "T"), "dot"), _n_(427404, "errors", lambda: errors))
            _l_(427406)
            _a_(427408, _n_(427407, "self", lambda: self), "w_")[0] += _a_(427410, _n_(427409, "self", lambda: self), "eta") * _c_(427413, _a_(427412, _n_(427411, "errors", lambda: errors), "sum"))
            _l_(427414)
            cost = _c_(427417, _a_(427416, (_n_(427415, "errors", lambda: errors)**2), "sum")) / 2.0
            _l_(427418)
            _c_(427423, _a_(427421, _a_(427420, _n_(427419, "self", lambda: self), "cost_"), "append"), _n_(427422, "cost", lambda: cost))
            _l_(427424)
        aux = _n_(427426, "self", lambda: self)
        _l_(427427)
        return aux

    def net_input(self, X):
        _l_(427438)

        aux = _c_(427434, _a_(427430, _n_(427429, "np", lambda: np), "dot"), _n_(427431, "X", lambda: X), _a_(427433, _n_(427432, "self", lambda: self), "w_")[1:]) + _a_(427436, _n_(427435, "self", lambda: self), "w_")[0]
        _l_(427437)
        return aux

    def predict(self, X):
        _l_(427444)

        aux = _c_(427442, _a_(427440, _n_(427439, "self", lambda: self), "net_input"), _n_(427441, "X", lambda: X))
        _l_(427443)
        return aux

    X = _a_(427445, racing[["BSP"]], "values")
    _l_(427446)
    y = _a_(427447, racing[["Position"]], "values")
    _l_(427448)
    try:
        from sklearn.preprocessing import StandardScaler
        _l_(427450)

    except ImportError:
        pass
    sc_X = _c_(427451, StandardScaler)
    _l_(427452)
    sc_y = _c_(427453, StandardScaler)
    _l_(427454)
    X_std = _c_(427456, _a_(427455, sc_X, "fit_transform"), X)
    _l_(427457)
    y_std = _c_(427459, _a_(427458, sc_y, "fit_transform"), y)
    _l_(427460)
    lr = _c_(427462, _n_(427461, "LinearRegressionGD", lambda: LinearRegressionGD))
    _l_(427463)
    _c_(427465, _a_(427464, lr, "fit"), X_std, y_std)
    _l_(427466)