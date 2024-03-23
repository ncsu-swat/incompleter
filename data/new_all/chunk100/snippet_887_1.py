# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def insertionSort(nlist):
    _l_(87209)

    for index in _c_(87189, _n_(87185, "range", lambda: range), 1, _c_(87188, _n_(87186, "len", lambda: len), _n_(87187, "nlist", lambda: nlist))):
        _l_(87208)

        position = _n_(87190, "index", lambda: index)
        _l_(87191)
        while _n_(87192, "position", lambda: position) > 0 and _n_(87193, "nlist", lambda: nlist)[_n_(87194, "position", lambda: position) - 1] > _n_(87195, "currentvalue", lambda: currentvalue):
            _l_(87203)

            _n_(87196, "nlist", lambda: nlist)[_n_(87197, "position", lambda: position)] = _n_(87198, "nlist", lambda: nlist)[_n_(87199, "position", lambda: position) - 1]
            _l_(87200)
            position = _n_(87201, "position", lambda: position) - 1
            _l_(87202)
        _n_(87204, "nlist", lambda: nlist)[_n_(87205, "position", lambda: position)] = _n_(87206, "currentvalue", lambda: currentvalue)
        _l_(87207)
nlist = [14, 46, 43, 27, 57, 41, 45, 21, 70]
_l_(87210)
_c_(87213, _n_(87211, "insertionSort", lambda: insertionSort), _n_(87212, "nlist", lambda: nlist))
_l_(87214)
_c_(87217, _n_(87215, "print", lambda: print), _n_(87216, "nlist", lambda: nlist))
_l_(87218)