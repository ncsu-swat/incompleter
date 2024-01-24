# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53715516/attribute-error-traintype-object-has-no-attribute-v-attribute-should-have
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import math
    _l_(532711)

except ImportError:
    pass

class TrainType(_n_(532712, "object", lambda: object)):
    _l_(532732)

    def __init__(self,t,M,n,L,S,pas):
        _l_(532731)

        _n_(532713, "self", lambda: self).t = _n_(532714, "t", lambda: t)              # train model
        _l_(532715)              # train model
        _n_(532716, "self", lambda: self).M = _n_(532717, "M", lambda: M)              # train mass [t]
        _l_(532718)              # train mass [t]
        _n_(532719, "self", lambda: self).n = _n_(532720, "n", lambda: n)              # numer of axles [-]
        _l_(532721)              # numer of axles [-]
        _n_(532722, "self", lambda: self).L = _n_(532723, "L", lambda: L)              # train length [m]
        _l_(532724)              # train length [m]
        _n_(532725, "self", lambda: self).S = _n_(532726, "S", lambda: S)              # crossection area [m2]
        _l_(532727)              # crossection area [m2]
        _n_(532728, "self", lambda: self).pas = _n_(532729, "pas", lambda: pas)          # passenger capacity [-]
        _l_(532730)          # passenger capacity [-]

# Running resistance force formula
def run_res(self,v):
    _l_(532754)

    C = 0.0035*_a_(532734, _n_(532733, "self", lambda: self), "S")+0.041*_a_(532736, _n_(532735, "self", lambda: self), "L")/100+0.002;
    _l_(532737)
    R_L = 9.81*(1.3*_c_(532744, _a_(532739, _n_(532738, "math", lambda: math), "sqrt"), 10*_a_(532741, _n_(532740, "self", lambda: self), "n")/_a_(532743, _n_(532742, "self", lambda: self), "M"))+0.01*_a_(532746, _n_(532745, "self", lambda: self), "v"))*_a_(532748, _n_(532747, "self", lambda: self), "M")+_n_(532749, "C", lambda: C)*_n_(532750, "v", lambda: v)**2
    _l_(532751)
    aux = _n_(532752, "R_L", lambda: R_L)
    _l_(532753)
    return aux

# Power required formula
def power(self,v):
    _l_(532765)

    a = _c_(532758, _a_(532756, _n_(532755, "self", lambda: self), "run_res"), _n_(532757, "v", lambda: v))
    _l_(532759)
    P = _n_(532760, "a", lambda: a)*_n_(532761, "v", lambda: v)
    _l_(532762)
    aux = _n_(532763, "P", lambda: P)
    _l_(532764)
    return aux

train1 = _c_(532767, _n_(532766, "TrainType", lambda: TrainType), "Talgo 350",323,21,200,10,318)
_l_(532768)

_c_(532773, _n_(532769, "print", lambda: print), _c_(532772, _a_(532771, _n_(532770, "train1", lambda: train1), "run_res"), 10))       # for test reasons v = 10
_l_(532774)       # for test reasons v = 10
_c_(532779, _n_(532775, "print", lambda: print), _c_(532778, _a_(532777, _n_(532776, "train1", lambda: train1), "power"), 10))
_l_(532780)