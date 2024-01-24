# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50779554/nameerror-name-gate-op-is-not-defined-tensorflow
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class GradientDescentOptimizer(_n_(389014, "Optimizer", lambda: Optimizer), _a_(389017, _a_(389016, _n_(389015, "tf", lambda: tf), "train"), "GradientDescentOptimizer")):
    _l_(389097)

    def compute_gradients(self, loss, var_list=None,
                        gate_gradients=GATE_OP,
                        aggregation_method=None,
                        colocate_gradients_with_ops=False,
                        grad_loss=None):
        _l_(389046)

        if _n_(389018, "var_list", lambda: var_list) is not None:
            _l_(389024)

            for v in _n_(389019, "var_list", lambda: var_list):
                _l_(389023)

                v = _n_(389020, "v", lambda: v) + _n_(389021, "epsilon", lambda: epsilon)
                _l_(389022)
        if _n_(389025, "var_list", lambda: var_list) is None:
            _l_(389035)

            var_list = _c_(389028, _a_(389027, _n_(389026, "utils", lambda: utils), "hyperparameters"))
            _l_(389029)
            for v in _n_(389030, "var_list", lambda: var_list):
                _l_(389034)

                v = _n_(389031, "v", lambda: v) + _n_(389032, "epsilon", lambda: epsilon)
                _l_(389033)
        grads_and_vars = _c_(389042, _a_(389039, _n_(389036, "super", lambda: super)(_n_(389037, "GradientOracle", lambda: GradientOracle), _n_(389038, "self", lambda: self)), "compute_gradients"), _n_(389040, "loss", lambda: loss), _n_(389041, "var_list", lambda: var_list))
        _l_(389043)
        aux = _n_(389044, "grads_and_vars", lambda: grads_and_vars)
        _l_(389045)
        return aux

    def apply_gradients(self, grads_and_vars, global_step=None, name=None):
        _l_(389078)

        ts = _c_(389054, _a_(389050, _n_(389047, "super", lambda: super)(_n_(389048, "GradientOracle", lambda: GradientOracle), _n_(389049, "self", lambda: self)), "apply_gradients"), _n_(389051, "grads_and_vars", lambda: grads_and_vars), _n_(389052, "global_step", lambda: global_step), _n_(389053, "name", lambda: name))
        _l_(389055)
        dynamics = _c_(389057, _n_(389056, "OrderedDict", lambda: OrderedDict))
        _l_(389058)
        for g, w in _n_(389059, "grads_and_vars", lambda: grads_and_vars):
            _l_(389074)

            wk = _n_(389060, "w", lambda: w) - _c_(389067, _a_(389062, _n_(389061, "tf", lambda: tf), "cast"), _a_(389064, _n_(389063, "self", lambda: self), "_learning_rate_tensor"), _a_(389066, _n_(389065, "g", lambda: g), "dtype")) * _n_(389068, "g", lambda: g)
            _l_(389069)
            _n_(389070, "dynamics", lambda: dynamics)[_n_(389071, "w", lambda: w)] = _n_(389072, "wk", lambda: wk)
            _l_(389073)
        aux = _n_(389075, "ts", lambda: ts), _n_(389076, "dynamics", lambda: dynamics)
        _l_(389077)
        return aux

    def __str__(self):
        _l_(389086)

        aux = _c_(389084, _a_(389079, '{}_lr{}', "format"), _a_(389081, _n_(389080, "self", lambda: self), "_name"), _a_(389083, _n_(389082, "self", lambda: self), "_learning_rate"))
        _l_(389085)
        return aux

    @_n_(389087, "property", lambda: property)
    def learning_rate(self):
        _l_(389091)

        aux = _a_(389089, _n_(389088, "self", lambda: self), "_learning_rate")
        _l_(389090)
        return aux

    @_n_(389092, "property", lambda: property)
    def learning_rate_tensor(self):
        _l_(389096)

        aux = _a_(389094, _n_(389093, "self", lambda: self), "_learning_rate_tensor")
        _l_(389095)
        return aux