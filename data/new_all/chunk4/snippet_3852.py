# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66496379/typeerror-cant-instantiate-abstract-class-ordergenaratorfortransfomer-with-abs
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(587886)

except ImportError:
    pass

class OrderGenaratorForTransfomer(_n_(587887, "Sequence", lambda: Sequence)):
    _l_(587915)

    n_products = 1000
    _l_(587888)
    n_windows = 10
    _l_(587889)
    n_customers = 10
    _l_(587890)
    def __init__(
        self
    ):
        _l_(587892)

        pass
        _l_(587891)

    def __getitem__(self, item):
        _l_(587914)

        X = _c_(587901, _a_(587894, _n_(587893, "np", lambda: np), "zeros"), (_a_(587896, _n_(587895, "self", lambda: self), "n_customers"), _a_(587898, _n_(587897, "self", lambda: self), "n_windows"), _a_(587900, _n_(587899, "self", lambda: self), "n_products")))
        _l_(587902)
        Y = _c_(587909, _a_(587904, _n_(587903, "np", lambda: np), "zeros"), (_a_(587906, _n_(587905, "self", lambda: self), "n_customers"), 1, _a_(587908, _n_(587907, "self", lambda: self), "n_products")))
        _l_(587910)
        aux = _n_(587911, "X", lambda: X), _n_(587912, "Y", lambda: Y)
        _l_(587913)

        return aux