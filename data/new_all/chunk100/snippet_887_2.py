# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def insertionSort(nlist):
    _l_(87246)

    for index in _c_(87223, _n_(87219, "range", lambda: range), 1, _c_(87222, _n_(87220, "len", lambda: len), _n_(87221, "nlist", lambda: nlist))):
        _l_(87245)

        currentvalue = _n_(87224, "nlist", lambda: nlist)[_n_(87225, "index", lambda: index)]
        _l_(87226)
        position = _n_(87227, "index", lambda: index)
        _l_(87228)
        while _n_(87229, "position", lambda: position) > 0 and _n_(87230, "nlist", lambda: nlist)[_n_(87231, "position", lambda: position) - 1] > _n_(87232, "currentvalue", lambda: currentvalue):
            _l_(87240)

            _n_(87233, "nlist", lambda: nlist)[_n_(87234, "position", lambda: position)] = _n_(87235, "nlist", lambda: nlist)[_n_(87236, "position", lambda: position) - 1]
            _l_(87237)
            position = _n_(87238, "position", lambda: position) - 1
            _l_(87239)
        _n_(87241, "nlist", lambda: nlist)[_n_(87242, "position", lambda: position)] = _n_(87243, "currentvalue", lambda: currentvalue)
        _l_(87244)
_c_(87249, _n_(87247, "insertionSort", lambda: insertionSort), _n_(87248, "nlist", lambda: nlist))
_l_(87250)
_c_(87253, _n_(87251, "print", lambda: print), _n_(87252, "nlist", lambda: nlist))
_l_(87254)