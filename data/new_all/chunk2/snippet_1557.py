# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/20014392/name-error-python-a-text-adventure-game
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from character import*
    _l_(425226)

except ImportError:
    pass
class player(_n_(425227, "character", lambda: character)):
    _l_(425244)

    def __init__(self,name,hp,maxhp,attack_damage,ability_power):
        _l_(425243)

        _c_(425235, _a_(425231, _n_(425228, "super", lambda: super)(_n_(425229, "player", lambda: player),_n_(425230, "self", lambda: self)), "__init__"), _n_(425232, "name", lambda: name), _n_(425233, "hp", lambda: hp), _n_(425234, "maxhp", lambda: maxhp))
        _l_(425236)
        _n_(425237, "self", lambda: self).attack_damage = _n_(425238, "attack_damage", lambda: attack_damage)
        _l_(425239)
        _n_(425240, "self", lambda: self).ability_power = _n_(425241, "ability_power", lambda: ability_power)
        _l_(425242)