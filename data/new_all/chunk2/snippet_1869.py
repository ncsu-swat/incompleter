# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/46503572/typeerror-required-argument-not-found-getitem-numpy
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(443531)

except ImportError:
    pass

class Myarray (_a_(443533, _n_(443532, "np", lambda: np), "ndarray")):
    _l_(443547)

    def __getitem__(self,n):
        _l_(443546)

        if _n_(443534, "n", lambda: n)<0:
            _l_(443538)

            raise _c_(443536, _n_(443535, "IndexError", lambda: IndexError), "...")
            _l_(443537)
        aux = _c_(443544, _a_(443541, _a_(443540, _n_(443539, "np", lambda: np), "ndarray"), "__getitem__"), _n_(443542, "self", lambda: self),_n_(443543, "n", lambda: n))
        _l_(443545)
        return aux

class Items(_n_(443548, "Myarray", lambda: Myarray)):
    _l_(443554)

    def __init__(self):
        _l_(443553)

        _c_(443551, _a_(443550, _n_(443549, "self", lambda: self), "load_tab"))
        _l_(443552)

class Item_I(_n_(443555, "Items", lambda: Items)):
    _l_(443562)

    def load_tab(self):
        _l_(443561)

        _n_(443556, "self", lambda: self).tab=_c_(443559, _a_(443558, _n_(443557, "np", lambda: np), "load"), "file.txt")
        _l_(443560)

a=_c_(443564, _n_(443563, "Item_I", lambda: Item_I))
_l_(443565)