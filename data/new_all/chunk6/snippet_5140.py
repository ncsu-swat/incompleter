# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/20023345/another-name-error-for-my-text-adventure-game-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(349869)

except ImportError:
    pass
try:
    from character import *
    _l_(349871)

except ImportError:
    pass
try:
    from player import *
    _l_(349873)

except ImportError:
    pass

class random_enemies(_n_(349874, "character", lambda: character)):
    _l_(349910)

    def __init__(self,name,hp,maxhp,attack_damage,ability_power,exp):
        _l_(349893)

        _c_(349882, _a_(349878, _n_(349875, "super", lambda: super)(_n_(349876, "random_enemies", lambda: random_enemies),_n_(349877, "self", lambda: self)), "__init__"), _n_(349879, "name", lambda: name),_n_(349880, "hp", lambda: hp),_n_(349881, "maxhp", lambda: maxhp))
        _l_(349883)
        _n_(349884, "self", lambda: self).attack_damage = _n_(349885, "attack_damage", lambda: attack_damage)
        _l_(349886)
        _n_(349887, "self", lambda: self).ability_power = _n_(349888, "ability_power", lambda: ability_power)
        _l_(349889)
        _n_(349890, "self", lambda: self).exp = _n_(349891, "exp", lambda: exp)
        _l_(349892)
    def weak():
        _l_(349909)

        _n_(349894, "self", lambda: self).hp = _c_(349901, _a_(349896, _n_(349895, "random", lambda: random), "randint"), _a_(349898, _n_(349897, "p", lambda: p), "maxhp")/10, _a_(349900, _n_(349899, "p", lambda: p), "maxhp")/5)
        _l_(349902)
        _n_(349903, "self", lambda: self).attack_damage = None
        _l_(349904)
        _n_(349905, "self", lambda: self).ability_power = None
        _l_(349906)
        _n_(349907, "self", lambda: self).exp = None
        _l_(349908)
try:
    from character import*
    _l_(349912)

except ImportError:
    pass
class player(_n_(349913, "character", lambda: character)):
    _l_(349930)

    def __init__(self,name,hp,maxhp,attack_damage,ability_power):
        _l_(349929)

        _c_(349921, _a_(349917, _n_(349914, "super", lambda: super)(_n_(349915, "player", lambda: player),_n_(349916, "self", lambda: self)), "__init__"), _n_(349918, "name", lambda: name), _n_(349919, "hp", lambda: hp), _n_(349920, "maxhp", lambda: maxhp))
        _l_(349922)
        _n_(349923, "self", lambda: self).attack_damage = _n_(349924, "attack_damage", lambda: attack_damage)
        _l_(349925)
        _n_(349926, "self", lambda: self).ability_power = _n_(349927, "ability_power", lambda: ability_power)
        _l_(349928)