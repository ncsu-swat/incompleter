# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/2709821/what-is-the-purpose-of-the-self-parameter-why-is-it-needed
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class C:
    _l_(1545043)

    def m1(self, arg):
        _l_(1545042)

        _c_(1545039, _n_(1545037, "print", lambda: print), _n_(1545038, "self", lambda: self), ' inside')
        _l_(1545040)
        pass
        _l_(1545041)

ci =_c_(1545045, _n_(1545044, "C", lambda: C))
_l_(1545046)
_c_(1545049, _n_(1545047, "print", lambda: print), _n_(1545048, "ci", lambda: ci), ' outside')
_l_(1545050)
_c_(1545053, _a_(1545052, _n_(1545051, "ci", lambda: ci), "m1"), None)
_l_(1545054)
_c_(1545061, _n_(1545055, "print", lambda: print), _c_(1545060, _n_(1545056, "hex", lambda: hex), _c_(1545059, _n_(1545057, "id", lambda: id), _n_(1545058, "ci", lambda: ci)))) # hex memory address
_l_(1545062) # hex memory address

0x2b9d79c6cc0
_l_(1545063)

