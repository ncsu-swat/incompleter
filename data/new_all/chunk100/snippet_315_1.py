# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def selectionSort(nlist):
    _l_(30200)

    for fillslot in _c_(30174, _n_(30170, "range", lambda: range), _c_(30173, _n_(30171, "len", lambda: len), _n_(30172, "nlist", lambda: nlist)) - 1, 0, -1):
        _l_(30199)

        maxpos = 0
        _l_(30175)
        for location in _c_(30178, _n_(30176, "range", lambda: range), 1, _n_(30177, "fillslot", lambda: fillslot) + 1):
            _l_(30186)

            if _n_(30179, "nlist", lambda: nlist)[_n_(30180, "location", lambda: location)] > _n_(30181, "nlist", lambda: nlist)[_n_(30182, "maxpos", lambda: maxpos)]:
                _l_(30185)

                maxpos = _n_(30183, "location", lambda: location)
                _l_(30184)
        temp = _n_(30187, "nlist", lambda: nlist)[_n_(30188, "fillslot", lambda: fillslot)]
        _l_(30189)
        _n_(30190, "nlist", lambda: nlist)[_n_(30191, "fillslot", lambda: fillslot)] = _n_(30192, "nlist", lambda: nlist)[_n_(30193, "maxpos", lambda: maxpos)]
        _l_(30194)
        _n_(30195, "nlist", lambda: nlist)[_n_(30196, "maxpos", lambda: maxpos)] = _n_(30197, "temp", lambda: temp)
        _l_(30198)
_c_(30203, _n_(30201, "selectionSort", lambda: selectionSort), _n_(30202, "nlist", lambda: nlist))
_l_(30204)
_c_(30207, _n_(30205, "print", lambda: print), _n_(30206, "nlist", lambda: nlist))
_l_(30208)