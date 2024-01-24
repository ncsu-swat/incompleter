# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74875654/typeerror-when-modifying-tf-keras-optimizer-parameter
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class AccumOptimizer(_a_(583271, _a_(583270, _a_(583269, _n_(583268, "tf", lambda: tf), "keras"), "optimizers"), "Optimizer")):
    _l_(583322)


    def __init__(self, optimizer, steps_per_update=1, **kwargs):
        _l_(583321)


        _c_(583277, _a_(583275, _n_(583272, "super", lambda: super)(_n_(583273, "AccumOptimizer", lambda: AccumOptimizer), _n_(583274, "self", lambda: self)), "__init__"), name="AccumOptimizer", **_n_(583276, "kwargs", lambda: kwargs))
        _l_(583278)
        _n_(583279, "self", lambda: self).optimizer = _n_(583280, "optimizer", lambda: optimizer)
        _l_(583281)
        _n_(583282, "self", lambda: self).steps_per_update = _n_(583283, "steps_per_update", lambda: steps_per_update)
        _l_(583284)
        _n_(583285, "self", lambda: self).iterations = _c_(583288, _a_(583287, _n_(583286, "tf", lambda: tf), "Variable"), 0, dtype='int64', name='iterations')
        _l_(583289)
        _n_(583290, "self", lambda: self).cond = _c_(583297, _a_(583292, _n_(583291, "tf", lambda: tf), "equal"), _a_(583294, _n_(583293, "self", lambda: self), "iterations") % _a_(583296, _n_(583295, "self", lambda: self), "steps_per_update"), 0)
        _l_(583298)
        _n_(583299, "self", lambda: self).lr = _a_(583302, _a_(583301, _n_(583300, "self", lambda: self), "optimizer"), "learning_rate")
        _l_(583303)
        _a_(583305, _n_(583304, "self", lambda: self), "optimizer").learning_rate = _c_(583318, _a_(583307, _n_(583306, "tf", lambda: tf), "cond"), _a_(583309, _n_(583308, "self", lambda: self), "cond"),
                                               lambda: _a_(583312, _a_(583311, _n_(583310, "self", lambda: self), "optimizer"), "learning_rate"),
                                               lambda: _c_(583317, _a_(583314, _n_(583313, "tf", lambda: tf), "constant"), 0, _a_(583316, _n_(583315, "tf", lambda: tf), "float32")))
        _l_(583319)
        ...
        _l_(583320)