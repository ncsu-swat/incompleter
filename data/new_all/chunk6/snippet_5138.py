# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/20023345/another-name-error-for-my-text-adventure-game-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(371985)

except ImportError:
    pass
try:
    from character import *
    _l_(371987)

except ImportError:
    pass
try:
    from player import *
    _l_(371989)

except ImportError:
    pass

class random_enemies(_n_(371990, "character", lambda: character)):
    _l_(372026)

    def __init__(self,name,hp,maxhp,attack_damage,ability_power,exp):
        _l_(372009)

        _c_(371998, _a_(371994, _n_(371991, "super", lambda: super)(_n_(371992, "random_enemies", lambda: random_enemies),_n_(371993, "self", lambda: self)), "__init__"), _n_(371995, "name", lambda: name),_n_(371996, "hp", lambda: hp),_n_(371997, "maxhp", lambda: maxhp))
        _l_(371999)
        _n_(372000, "self", lambda: self).attack_damage = _n_(372001, "attack_damage", lambda: attack_damage)
        _l_(372002)
        _n_(372003, "self", lambda: self).ability_power = _n_(372004, "ability_power", lambda: ability_power)
        _l_(372005)
        _n_(372006, "self", lambda: self).exp = _n_(372007, "exp", lambda: exp)
        _l_(372008)
    def weak():
        _l_(372025)

        _n_(372010, "self", lambda: self).hp = _c_(372017, _a_(372012, _n_(372011, "random", lambda: random), "randint"), _a_(372014, _n_(372013, "p", lambda: p), "maxhp")/10, _a_(372016, _n_(372015, "p", lambda: p), "maxhp")/5)
        _l_(372018)
        _n_(372019, "self", lambda: self).attack_damage = None
        _l_(372020)
        _n_(372021, "self", lambda: self).ability_power = None
        _l_(372022)
        _n_(372023, "self", lambda: self).exp = None
        _l_(372024)
try:
    from character import*
    _l_(372028)

except ImportError:
    pass
class player(_n_(372029, "character", lambda: character)):
    _l_(372046)

    def __init__(self,name,hp,maxhp,attack_damage,ability_power):
        _l_(372045)

        _c_(372037, _a_(372033, _n_(372030, "super", lambda: super)(_n_(372031, "player", lambda: player),_n_(372032, "self", lambda: self)), "__init__"), _n_(372034, "name", lambda: name), _n_(372035, "hp", lambda: hp), _n_(372036, "maxhp", lambda: maxhp))
        _l_(372038)
        _n_(372039, "self", lambda: self).attack_damage = _n_(372040, "attack_damage", lambda: attack_damage)
        _l_(372041)
        _n_(372042, "self", lambda: self).ability_power = _n_(372043, "ability_power", lambda: ability_power)
        _l_(372044)