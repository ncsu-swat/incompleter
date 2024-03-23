# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def insertionSort(nlist):
    _l_(87175)

    for index in _c_(87154, _n_(87150, "range", lambda: range), 1, _c_(87153, _n_(87151, "len", lambda: len), _n_(87152, "nlist", lambda: nlist))):
        _l_(87174)

        currentvalue = _n_(87155, "nlist", lambda: nlist)[_n_(87156, "index", lambda: index)]
        _l_(87157)
        position = _n_(87158, "index", lambda: index)
        _l_(87159)
        while _n_(87160, "position", lambda: position) > 0 and _n_(87161, "nlist", lambda: nlist)[_n_(87162, "position", lambda: position) - 1] > _n_(87163, "currentvalue", lambda: currentvalue):
            _l_(87169)

            _n_(87164, "nlist", lambda: nlist)[_n_(87165, "position", lambda: position)] = _n_(87166, "nlist", lambda: nlist)[_n_(87167, "position", lambda: position) - 1]
            _l_(87168)
        _n_(87170, "nlist", lambda: nlist)[_n_(87171, "position", lambda: position)] = _n_(87172, "currentvalue", lambda: currentvalue)
        _l_(87173)
nlist = [14, 46, 43, 27, 57, 41, 45, 21, 70]
_l_(87176)
_c_(87179, _n_(87177, "insertionSort", lambda: insertionSort), _n_(87178, "nlist", lambda: nlist))
_l_(87180)
_c_(87183, _n_(87181, "print", lambda: print), _n_(87182, "nlist", lambda: nlist))
_l_(87184)