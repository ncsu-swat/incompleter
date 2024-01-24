# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51315053/nameerror-while-trying-to-extend-a-class
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from pokemon import *
    _l_(540948)

except ImportError:
    pass
class Charmander(_n_(540949, "Pokemon", lambda: Pokemon)):
    _l_(540974)

    pass
    _l_(540950)
    def __init__(self, current_hp, attack, defense):
        _l_(540961)

        _n_(540951, "self", lambda: self).name = "Charmander"
        _l_(540952)
        _n_(540953, "self", lambda: self).type = "Fire"
        _l_(540954)
        _n_(540955, "self", lambda: self).current_hp = 200
        _l_(540956)
        _n_(540957, "self", lambda: self).attack = 10
        _l_(540958)
        _n_(540959, "self", lambda: self).defense = 10
        _l_(540960)

    def ember(self, opponent):
        _l_(540966)

        _c_(540964, _a_(540963, _n_(540962, "opponent", lambda: opponent), "takeDamage"), 40)
        _l_(540965)

    def will_o_wisp(self, opponent):
        _l_(540968)

        aux = ""
        _l_(540967)
        return aux

    def flamethrower(self, opponent):
        _l_(540973)

        _c_(540971, _a_(540970, _n_(540969, "opponent", lambda: opponent), "takeDamage"), 90)
        _l_(540972)