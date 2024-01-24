# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53727834/scipy-minimization-typeerror-int-object-is-not-callable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(409684)

except ImportError:
    pass
try:
    import numpy as np
    _l_(409686)

except ImportError:
    pass
try:
    from scipy.optimize import minimize
    _l_(409688)

except ImportError:
    pass

def objective (h, b, Ip, Im, NIt, s, Qt):
    _l_(409694)

    aux = _n_(409689, "h", lambda: h)*_n_(409690, "Ip", lambda: Ip)+_n_(409691, "b", lambda: b)*_n_(409692, "Im", lambda: Im)
    _l_(409693)
    return aux

def constraint1 (h, b, Ip, Im, NIt, s, Qt):
    _l_(409698)

    aux = _n_(409695, "NIt", lambda: NIt)-_n_(409696, "s", lambda: s)
    _l_(409697)
    return aux

def constraint2 (h, b, Ip, Im, NIt, s, Qt):
    _l_(409701)

    aux = _n_(409699, "Qt", lambda: Qt)
    _l_(409700)
    return aux

def test(T, d, RT, LT, h, b, I0, s):
    _l_(409823)

    i = 1
    _l_(409702)
    It = [0] * _n_(409703, "T", lambda: T)
    _l_(409704)
    Qt = [0] * _n_(409705, "T", lambda: T)
    _l_(409706)
    NIt = [0] * _n_(409707, "T", lambda: T)
    _l_(409708)
    _n_(409709, "It", lambda: It)[0] = _n_(409710, "I0", lambda: I0) - _n_(409711, "d", lambda: d)[0]
    _l_(409712)
    _n_(409713, "Qt", lambda: Qt)[0] = _n_(409714, "d", lambda: d)[0]
    _l_(409715)
    _n_(409716, "NIt", lambda: NIt)[0] = _n_(409717, "I0", lambda: I0)
    _l_(409718)
    while _n_(409719, "i", lambda: i) < _n_(409720, "T", lambda: T):
        _l_(409818)

        if (_n_(409721, "i", lambda: i) - _n_(409722, "LT", lambda: LT)) >= 0:
            _l_(409740)

            _n_(409723, "It", lambda: It)[_n_(409724, "i", lambda: i)] = _n_(409725, "It", lambda: It)[_n_(409726, "i", lambda: i)-1] - _n_(409727, "d", lambda: d)[_n_(409728, "i", lambda: i)] + _n_(409729, "Qt", lambda: Qt)[_n_(409730, "i", lambda: i)-_n_(409731, "LT", lambda: LT)]
            _l_(409732)
        else:
            _n_(409733, "It", lambda: It)[_n_(409734, "i", lambda: i)] = _n_(409735, "It", lambda: It)[_n_(409736, "i", lambda: i)-1] - _n_(409737, "d", lambda: d)[_n_(409738, "i", lambda: i)]
            _l_(409739)
        _n_(409741, "NIt", lambda: NIt)[_n_(409742, "i", lambda: i)] = _n_(409743, "NIt", lambda: NIt)[_n_(409744, "i", lambda: i)-1] - _n_(409745, "d", lambda: d)[_n_(409746, "i", lambda: i)-1] + _n_(409747, "Qt", lambda: Qt)[_n_(409748, "i", lambda: i)-1]
        _l_(409749)
        if _n_(409750, "It", lambda: It)[_n_(409751, "i", lambda: i)-1] > 0:
            _l_(409756)

            Ip = _n_(409752, "It", lambda: It)[_n_(409753, "i", lambda: i)-1]
            _l_(409754)
            Im = 0
            _l_(409755)
        if _n_(409757, "It", lambda: It)[_n_(409758, "i", lambda: i)-1] < 0:
            _l_(409763)

            Ip = 0
            _l_(409759)
            Im = _n_(409760, "It", lambda: It)[_n_(409761, "i", lambda: i)-1]
            _l_(409762)
        if _n_(409764, "It", lambda: It)[_n_(409765, "i", lambda: i)-1] == 0:
            _l_(409768)

            Ip = 0
            _l_(409766)
            Im = 0
            _l_(409767)

        x0 = [_n_(409769, "h", lambda: h), _n_(409770, "b", lambda: b), _n_(409771, "Ip", lambda: Ip), _n_(409772, "Im", lambda: Im), _n_(409773, "NIt", lambda: NIt)[_n_(409774, "i", lambda: i)], _n_(409775, "s", lambda: s), _n_(409776, "Qt", lambda: Qt)[_n_(409777, "i", lambda: i)]]
        _l_(409778)
        con1 = {'type': 'ineq', 'fun': _c_(409789, _n_(409779, "constraint1", lambda: constraint1), _n_(409780, "h", lambda: h), _n_(409781, "b", lambda: b), _n_(409782, "Ip", lambda: Ip), _n_(409783, "Im", lambda: Im), _n_(409784, "NIt", lambda: NIt)[_n_(409785, "i", lambda: i)], _n_(409786, "s", lambda: s), 
_n_(409787, "Qt", lambda: Qt)[_n_(409788, "i", lambda: i)])}
        _l_(409790)
        con2 = {'type': 'ineq', 'fun': _c_(409801, _n_(409791, "constraint2", lambda: constraint2), _n_(409792, "h", lambda: h), _n_(409793, "b", lambda: b), _n_(409794, "Ip", lambda: Ip), _n_(409795, "Im", lambda: Im), _n_(409796, "NIt", lambda: NIt)[_n_(409797, "i", lambda: i)], _n_(409798, "s", lambda: s), 
_n_(409799, "Qt", lambda: Qt)[_n_(409800, "i", lambda: i)])}
        _l_(409802)
        cons = [_n_(409803, "con1", lambda: con1), _n_(409804, "con2", lambda: con2)]
        _l_(409805)
        sol = _c_(409810, _n_(409806, "minimize", lambda: minimize), _n_(409807, "objective", lambda: objective), _n_(409808, "x0", lambda: x0), constraints=_n_(409809, "cons", lambda: cons))
        _l_(409811)

        _n_(409812, "Qt", lambda: Qt)[_n_(409813, "i", lambda: i)] = _a_(409815, _n_(409814, "sol", lambda: sol), "Qt")
        _l_(409816)
        i += 1
        _l_(409817)
    aux = _n_(409819, "It", lambda: It), _n_(409820, "NIt", lambda: NIt), _n_(409821, "Qt", lambda: Qt)
    _l_(409822)
    return aux

d = []
_l_(409824)
for j in _c_(409826, _n_(409825, "range", lambda: range), 30):
    _l_(409834)

    _c_(409832, _a_(409828, _n_(409827, "d", lambda: d), "append"), _c_(409831, _a_(409830, _n_(409829, "random", lambda: random), "randint"), 0, 2)) 
    _l_(409833) 

[It, NIt, Qt] = _c_(409837, _n_(409835, "test", lambda: test), 30, _n_(409836, "d", lambda: d), 1, 1, 1, 1, 1, 2)
_l_(409838)