# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/20014392/name-error-python-a-text-adventure-game
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from items import *
    _l_(436421)

except ImportError:
    pass

class weapons(_n_(436422, "Item", lambda: Item)):
    _l_(436438)

    def __init__(self, name, attack_damage, lifesteal = 0):
        _l_(436437)

        _c_(436429, _a_(436426, _n_(436423, "super", lambda: super)(_n_(436424, "weapons", lambda: weapons),_n_(436425, "self", lambda: self)), "__init__"), _n_(436427, "name", lambda: name), _n_(436428, "value", lambda: value), quantity=1)
        _l_(436430)
        _n_(436431, "self", lambda: self).attack_damage = _n_(436432, "attack_damage", lambda: attack_damage)
        _l_(436433)
        _n_(436434, "self", lambda: self).lifesteal = _n_(436435, "lifesteal", lambda: lifesteal)
        _l_(436436)