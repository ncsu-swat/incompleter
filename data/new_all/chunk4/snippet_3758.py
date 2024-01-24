# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68500183/class-in-python-3-9-4-gives-inconsistent-attribute-error-when-calling-method
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class DataSharer:
    _l_(626154)

    def __init__(self):
        _l_(626143)

        pass
        _l_(626142)

    def share_knowledge(self, forager_a, forager_b):
        _l_(626153)

        data = _c_(626146, _a_(626145, _n_(626144, "forager_a", lambda: forager_a), "share_heatmap_knowledge"))
        _l_(626147)
        _c_(626151, _a_(626149, _n_(626148, "forager_b", lambda: forager_b), "receive_heatmap_knowledge"), _n_(626150, "data", lambda: data))
        _l_(626152)


forager_a = _c_(626156, _n_(626155, "ForagerAgent", lambda: ForagerAgent))
_l_(626157)
_n_(626158, "forager_a", lambda: forager_a).heatmap = {'stock_1': 100.0, 'stock_2': 0}
_l_(626159)

forager_b = _c_(626161, _n_(626160, "ForagerAgent", lambda: ForagerAgent))
_l_(626162)
_n_(626163, "forager_b", lambda: forager_b).heatmap = {'stock_1': 0, 'stock_2': 15}
_l_(626164)

data_sharer = _c_(626166, _n_(626165, "DataSharer", lambda: DataSharer))
_l_(626167)
_c_(626172, _a_(626169, _n_(626168, "data_sharer", lambda: data_sharer), "share_knowledge"), forager_a=_n_(626170, "forager_a", lambda: forager_a), forager_b=_n_(626171, "forager_b", lambda: forager_b))
_l_(626173)