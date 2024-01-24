# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/44857367/in-python-3-x-typeerror-unsupported-operand-types-for-complex-and-comp
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Test():
    _l_(662013)

    def __init__(self):
        _l_(662004)

        _n_(662002, "self", lambda: self)._x=(1,2)
        _l_(662003)
    def __div__(self,div_fraction):
        _l_(662012)

        aux = (_a_(662006, _n_(662005, "self", lambda: self), "_x")[0]*_n_(662007, "div_fraction", lambda: div_fraction)[1],_a_(662009, _n_(662008, "self", lambda: self), "_x")[1]*_n_(662010, "div_fraction", lambda: div_fraction)[0])
        _l_(662011)
        return aux

y=_c_(662015, _n_(662014, "Test", lambda: Test))
_l_(662016)
z=_n_(662017, "y", lambda: y)/(1,3)
_l_(662018)
_c_(662021, _n_(662019, "print", lambda: print), _n_(662020, "z", lambda: z))
_l_(662022)