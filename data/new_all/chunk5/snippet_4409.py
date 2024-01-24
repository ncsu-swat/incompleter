# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58167836/monte-carlo-integral-typeerror-not-supported-between-instances-of-complex
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(657689)

except ImportError:
    pass
try:
    import numpy as np
    _l_(657691)

except ImportError:
    pass
try:
    import matplotlib
    _l_(657693)

except ImportError:
    pass
_c_(657696, _a_(657695, _n_(657694, "matplotlib", lambda: matplotlib), "use"), 'tkagg')
_l_(657697)
try:
    import matplotlib.pyplot as plt
    _l_(657699)

except ImportError:
    pass

def montecarlo(functie1,x1,x2,y1,y2):
    _l_(657808)

    f = _c_(657702, _n_(657700, "functie1", lambda: functie1), _n_(657701, "x", lambda: x))
    _l_(657703)
    true_point_x = []
    _l_(657704)
    true_point_y = []
    _l_(657705)
    false_point_x = []
    _l_(657706)
    false_point_y = []
    _l_(657707)
    positive_true = 0 
    _l_(657708) 
    negative_true = 0
    _l_(657709)
    n = 100000
    _l_(657710)

    for i in _c_(657713, _n_(657711, "range", lambda: range), _n_(657712, "n", lambda: n)):
        _l_(657782)

        x = (_n_(657714, "x2", lambda: x2)-_n_(657715, "x1", lambda: x1)) * _c_(657718, _a_(657717, _n_(657716, "random", lambda: random), "random")) + _n_(657719, "x1", lambda: x1)
        _l_(657720)
        y = (_n_(657721, "y2", lambda: y2)-_n_(657722, "y1", lambda: y1)) * _c_(657725, _a_(657724, _n_(657723, "random", lambda: random), "random")) + _n_(657726, "y1", lambda: y1)
        _l_(657727)
        if _n_(657728, "f", lambda: f) > 0:
            _l_(657781)

            if _n_(657729, "y", lambda: y) <= _n_(657730, "f", lambda: f) and _n_(657731, "y", lambda: y) > 0:
                _l_(657754)

                _c_(657735, _a_(657733, _n_(657732, "true_point_x", lambda: true_point_x), "append"), _n_(657734, "x", lambda: x))
                _l_(657736)
                _c_(657740, _a_(657738, _n_(657737, "true_point_y", lambda: true_point_y), "append"), _n_(657739, "y", lambda: y))
                _l_(657741)
                positive_true += 1
                _l_(657742)
            else:
                _c_(657746, _a_(657744, _n_(657743, "false_point_x", lambda: false_point_x), "append"), _n_(657745, "x", lambda: x))
                _l_(657747)
                _c_(657751, _a_(657749, _n_(657748, "false_point_y", lambda: false_point_y), "append"), _n_(657750, "y", lambda: y))
                _l_(657752)
                negative_true += 1
                _l_(657753)
        else:
            if _n_(657755, "y", lambda: y) >= _n_(657756, "f", lambda: f) and _n_(657757, "y", lambda: y) < 0:
                _l_(657780)

                _c_(657761, _a_(657759, _n_(657758, "true_point_x", lambda: true_point_x), "append"), _n_(657760, "x", lambda: x))
                _l_(657762)
                _c_(657766, _a_(657764, _n_(657763, "true_point_y", lambda: true_point_y), "append"), _n_(657765, "y", lambda: y))
                _l_(657767)
                positive_true -= 1
                _l_(657768)
            else:
                _c_(657772, _a_(657770, _n_(657769, "false_point_x", lambda: false_point_x), "append"), _n_(657771, "x", lambda: x))
                _l_(657773)
                _c_(657777, _a_(657775, _n_(657774, "false_point_y", lambda: false_point_y), "append"), _n_(657776, "y", lambda: y))
                _l_(657778)
                negative_true += 1
                _l_(657779)

    _c_(657787, _a_(657784, _n_(657783, "plt", lambda: plt), "plot"), _n_(657785, "true_point_x", lambda: true_point_x),_n_(657786, "true_point_y", lambda: true_point_y), 'o', markerfacecolor='g', markeredgecolor='k')
    _l_(657788)
    _c_(657793, _a_(657790, _n_(657789, "plt", lambda: plt), "plot"), _n_(657791, "false_point_x", lambda: false_point_x),_n_(657792, "false_point_y", lambda: false_point_y), 'o', markerfacecolor='r', markeredgecolor='k')
    _l_(657794)
    _c_(657797, _a_(657796, _n_(657795, "plt", lambda: plt), "show"))
    _l_(657798)

    surface = (_n_(657799, "x2", lambda: x2)-_n_(657800, "x1", lambda: x1))*(_n_(657801, "y2", lambda: y2)-_n_(657802, "y1", lambda: y1))
    _l_(657803)
    integral = _n_(657804, "surface", lambda: surface) * _n_(657805, "positive_true", lambda: positive_true) / _n_(657806, "n", lambda: n)
    _l_(657807)
def functie1(x):
    _l_(657812)

    aux = _n_(657809, "x", lambda: x) ** (_n_(657810, "x", lambda: x) + 0.5)
    _l_(657811)
    return aux
_c_(657815, _n_(657813, "montecarlo", lambda: montecarlo), _n_(657814, "functie1", lambda: functie1), -1, 2.2, -1, 1)
_l_(657816)