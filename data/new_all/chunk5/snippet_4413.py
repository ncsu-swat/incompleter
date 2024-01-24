# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58167836/monte-carlo-integral-typeerror-not-supported-between-instances-of-complex
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(673259)

except ImportError:
    pass
try:
    import numpy as np
    _l_(673261)

except ImportError:
    pass
try:
    import matplotlib
    _l_(673263)

except ImportError:
    pass
_c_(673266, _a_(673265, _n_(673264, "matplotlib", lambda: matplotlib), "use"), 'tkagg')
_l_(673267)
try:
    import matplotlib.pyplot as plt
    _l_(673269)

except ImportError:
    pass

def montecarlo(functie1,x1,x2,y1,y2):
    _l_(673378)

    f = _c_(673272, _n_(673270, "functie1", lambda: functie1), _n_(673271, "x", lambda: x))
    _l_(673273)
    true_point_x = []
    _l_(673274)
    true_point_y = []
    _l_(673275)
    false_point_x = []
    _l_(673276)
    false_point_y = []
    _l_(673277)
    positive_true = 0 
    _l_(673278) 
    negative_true = 0
    _l_(673279)
    n = 100000
    _l_(673280)

    for i in _c_(673283, _n_(673281, "range", lambda: range), _n_(673282, "n", lambda: n)):
        _l_(673352)

        x = (_n_(673284, "x2", lambda: x2)-_n_(673285, "x1", lambda: x1)) * _c_(673288, _a_(673287, _n_(673286, "random", lambda: random), "random")) + _n_(673289, "x1", lambda: x1)
        _l_(673290)
        y = (_n_(673291, "y2", lambda: y2)-_n_(673292, "y1", lambda: y1)) * _c_(673295, _a_(673294, _n_(673293, "random", lambda: random), "random")) + _n_(673296, "y1", lambda: y1)
        _l_(673297)
        if _n_(673298, "f", lambda: f) > 0:
            _l_(673351)

            if _n_(673299, "y", lambda: y) <= _n_(673300, "f", lambda: f) and _n_(673301, "y", lambda: y) > 0:
                _l_(673324)

                _c_(673305, _a_(673303, _n_(673302, "true_point_x", lambda: true_point_x), "append"), _n_(673304, "x", lambda: x))
                _l_(673306)
                _c_(673310, _a_(673308, _n_(673307, "true_point_y", lambda: true_point_y), "append"), _n_(673309, "y", lambda: y))
                _l_(673311)
                positive_true += 1
                _l_(673312)
            else:
                _c_(673316, _a_(673314, _n_(673313, "false_point_x", lambda: false_point_x), "append"), _n_(673315, "x", lambda: x))
                _l_(673317)
                _c_(673321, _a_(673319, _n_(673318, "false_point_y", lambda: false_point_y), "append"), _n_(673320, "y", lambda: y))
                _l_(673322)
                negative_true += 1
                _l_(673323)
        else:
            if _n_(673325, "y", lambda: y) >= _n_(673326, "f", lambda: f) and _n_(673327, "y", lambda: y) < 0:
                _l_(673350)

                _c_(673331, _a_(673329, _n_(673328, "true_point_x", lambda: true_point_x), "append"), _n_(673330, "x", lambda: x))
                _l_(673332)
                _c_(673336, _a_(673334, _n_(673333, "true_point_y", lambda: true_point_y), "append"), _n_(673335, "y", lambda: y))
                _l_(673337)
                positive_true -= 1
                _l_(673338)
            else:
                _c_(673342, _a_(673340, _n_(673339, "false_point_x", lambda: false_point_x), "append"), _n_(673341, "x", lambda: x))
                _l_(673343)
                _c_(673347, _a_(673345, _n_(673344, "false_point_y", lambda: false_point_y), "append"), _n_(673346, "y", lambda: y))
                _l_(673348)
                negative_true += 1
                _l_(673349)

    _c_(673357, _a_(673354, _n_(673353, "plt", lambda: plt), "plot"), _n_(673355, "true_point_x", lambda: true_point_x),_n_(673356, "true_point_y", lambda: true_point_y), 'o', markerfacecolor='g', markeredgecolor='k')
    _l_(673358)
    _c_(673363, _a_(673360, _n_(673359, "plt", lambda: plt), "plot"), _n_(673361, "false_point_x", lambda: false_point_x),_n_(673362, "false_point_y", lambda: false_point_y), 'o', markerfacecolor='r', markeredgecolor='k')
    _l_(673364)
    _c_(673367, _a_(673366, _n_(673365, "plt", lambda: plt), "show"))
    _l_(673368)

    surface = (_n_(673369, "x2", lambda: x2)-_n_(673370, "x1", lambda: x1))*(_n_(673371, "y2", lambda: y2)-_n_(673372, "y1", lambda: y1))
    _l_(673373)
    integral = _n_(673374, "surface", lambda: surface) * _n_(673375, "positive_true", lambda: positive_true) / _n_(673376, "n", lambda: n)
    _l_(673377)
def functie1(x):
    _l_(673382)

    aux = _n_(673379, "x", lambda: x) ** (_n_(673380, "x", lambda: x) + 0.5)
    _l_(673381)
    return aux
_c_(673385, _n_(673383, "montecarlo", lambda: montecarlo), _n_(673384, "functie1", lambda: functie1), -1, 2.2, -1, 1)
_l_(673386)