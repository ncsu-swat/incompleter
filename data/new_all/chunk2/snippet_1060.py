# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/48447149/typeerror-in-tensorflow-scipyoptimizerinterface-when-using-in-keras
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class CGTFOptimizer(_n_(438176, "object", lambda: object)):
    _l_(438189)

    def compute_gradients(self, loss, params):
        _l_(438188)

        optimizer = _c_(438179, _n_(438177, "ScipyOptimizerInterface", lambda: ScipyOptimizerInterface), _n_(438178, "loss", lambda: loss), method='cg')
        _l_(438180)
        result = _c_(438184, _a_(438182, _n_(438181, "optimizer", lambda: optimizer), "minimize"), _n_(438183, "loss", lambda: loss))
        _l_(438185)
        aux = _n_(438186, "result", lambda: result)
        _l_(438187)
        return aux

class CGTF(_n_(438190, "TFOptimizer", lambda: TFOptimizer)):
    _l_(438200)

    """ Wrapper for TFOptimizer """
    def __init__(self):
        _l_(438199)

        _c_(438197, _a_(438194, _n_(438191, "super", lambda: super)(_n_(438192, "CGTF", lambda: CGTF), _n_(438193, "self", lambda: self)), "__init__"), optimizer=_c_(438196, _n_(438195, "CGTFOptimizer", lambda: CGTFOptimizer)))
        _l_(438198)