# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/30174847/typeerror-attack-missing-1-required-positional-argument-self
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Enemmy :
    _l_(416144)

    life = 3
    _l_(416124)
    self = ""
    _l_(416125)
    def attack(self):
        _l_(416131)

        _c_(416127, _n_(416126, "print", lambda: print), "ouch!!!!")
        _l_(416128)
        _n_(416129, "self", lambda: self).life -= 1
        _l_(416130)

    def checkLife(self):
        _l_(416143)

        if _a_(416133, _n_(416132, "self", lambda: self), "life") <= 0 :
            _l_(416142)

            _c_(416135, _n_(416134, "print", lambda: print), "dead")
            _l_(416136)
        else:
            _c_(416140, _n_(416137, "print", lambda: print), _a_(416139, _n_(416138, "self", lambda: self), "life"))
            _l_(416141)

enemy=_n_(416145, "Enemmy", lambda: Enemmy)
_l_(416146)
_c_(416149, _a_(416148, _n_(416147, "enemy", lambda: enemy), "attack"))
_l_(416150)