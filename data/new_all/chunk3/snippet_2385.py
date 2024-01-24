# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/47103106/python3-subclass-is-being-instantiated-as-superclass-subclass-method-not-found
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from pydealer import Deck
    _l_(534436)

except ImportError:
    pass
try:
    from player import Player
    _l_(534438)

except ImportError:
    pass
try:
    from dealer import Dealer
    _l_(534440)

except ImportError:
    pass

class Table:
    _l_(534489)


    shoe = None
    _l_(534441)
    dealer = None
    _l_(534442)
    player = None
    _l_(534443)

    def __init__(self):
        _l_(534464)

        _n_(534444, "self", lambda: self).shoe = _c_(534446, _n_(534445, "Deck", lambda: Deck))
        _l_(534447)
        _a_(534449, _n_(534448, "self", lambda: self), "shoe").rebuild = True
        _l_(534450)
        _c_(534454, _a_(534453, _a_(534452, _n_(534451, "self", lambda: self), "shoe"), "shuffle"))
        _l_(534455)
        _n_(534456, "self", lambda: self).player = _c_(534458, _n_(534457, "Player", lambda: Player))
        _l_(534459)
        _n_(534460, "self", lambda: self).dealer = _c_(534462, _n_(534461, "Dealer", lambda: Dealer))
        _l_(534463)

    def start(self):
        _l_(534488)

        _c_(534468, _a_(534467, _a_(534466, _n_(534465, "self", lambda: self), "player"), "bet"))
        _l_(534469)
        _c_(534477, _a_(534472, _a_(534471, _n_(534470, "self", lambda: self), "dealer"), "deal"), _c_(534476, _a_(534475, _a_(534474, _n_(534473, "self", lambda: self), "shoe"), "deal"), 2))
        _l_(534478)
        _c_(534486, _a_(534481, _a_(534480, _n_(534479, "self", lambda: self), "player"), "deal"), _c_(534485, _a_(534484, _a_(534483, _n_(534482, "self", lambda: self), "shoe"), "deal"), 2))
        _l_(534487)