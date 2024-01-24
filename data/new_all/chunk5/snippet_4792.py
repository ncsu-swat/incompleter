# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/44857367/in-python-3-x-typeerror-unsupported-operand-types-for-complex-and-comp
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Test():
    _l_(677002)

    def __init__(self):
        _l_(676993)

        _n_(676991, "self", lambda: self)._x=(1,2)
        _l_(676992)
    def __div__(self,div_fraction):
        _l_(677001)

        aux = (_a_(676995, _n_(676994, "self", lambda: self), "_x")[0]*_n_(676996, "div_fraction", lambda: div_fraction)[1],_a_(676998, _n_(676997, "self", lambda: self), "_x")[1]*_n_(676999, "div_fraction", lambda: div_fraction)[0])
        _l_(677000)
        return aux

y=_c_(677004, _n_(677003, "Test", lambda: Test))
_l_(677005)
z=_n_(677006, "y", lambda: y)/(1,3)
_l_(677007)
_c_(677010, _n_(677008, "print", lambda: print), _n_(677009, "z", lambda: z))
_l_(677011)