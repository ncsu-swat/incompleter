# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56951307/math-sqrt-results-in-typeerrorfloat-object-cannot-be-interpreted-as-an-intege
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
pd = _c_(445895, _n_(445894, "Power", lambda: Power))
_l_(445896)
num = _c_(445899, _a_(445898, _n_(445897, "pd", lambda: pd), "calc_num"))
_l_(445900)
cir_num = _c_(445906, _n_(445901, "int", lambda: int), _c_(445905, _a_(445903, _n_(445902, "math", lambda: math), "sqrt"), _n_(445904, "num", lambda: num)))**2
_l_(445907)
circles = []
_l_(445908)
filled = 0
_l_(445909)
while True:
    _l_(445957)

    for i in _c_(445915, _n_(445910, "range", lambda: range), _c_(445914, _a_(445912, _n_(445911, "math", lambda: math), "sqrt"), _n_(445913, "cir_num", lambda: cir_num))-1):
        _l_(445933)

        for j in _c_(445921, _n_(445916, "range", lambda: range), _c_(445920, _a_(445918, _n_(445917, "math", lambda: math), "sqrt"), _n_(445919, "cir_num", lambda: cir_num))-1):
            _l_(445932)

            c = _c_(445925, _n_(445922, "Circle", lambda: Circle), _n_(445923, "frame", lambda: frame), _n_(445924, "cir_num", lambda: cir_num))
            _l_(445926)
            _c_(445930, _a_(445928, _n_(445927, "circles", lambda: circles), "append"), _n_(445929, "c", lambda: c))
            _l_(445931)
    ##drawing
    for c in _n_(445934, "circles", lambda: circles):
        _l_(445949)

        if _a_(445936, _n_(445935, "c", lambda: c), "stage") == 'empty':
            _l_(445948)

            _c_(445939, _a_(445938, _n_(445937, "c", lambda: c), "draw_empty"))
            _l_(445940)
        elif _a_(445942, _n_(445941, "c", lambda: c), "stage") == 'filled':
            _l_(445947)

            _c_(445945, _a_(445944, _n_(445943, "c", lambda: c), "draw_filled"))
            _l_(445946)
    avar = 0
    _l_(445950)
    for c in _n_(445951, "circles", lambda: circles):
        _l_(445954)

        avar += _n_(445952, "c", lambda: c).num2
        _l_(445953)
    filled += _n_(445955, "avar", lambda: avar)
    _l_(445956)