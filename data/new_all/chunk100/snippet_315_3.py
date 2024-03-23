# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def selectionSort(nlist):
    _l_(30238)

    for fillslot in _c_(30213, _n_(30209, "range", lambda: range), _c_(30212, _n_(30210, "len", lambda: len), _n_(30211, "nlist", lambda: nlist)) - 1, 0, -1):
        _l_(30237)

        for location in _c_(30216, _n_(30214, "range", lambda: range), 1, _n_(30215, "fillslot", lambda: fillslot) + 1):
            _l_(30224)

            if _n_(30217, "nlist", lambda: nlist)[_n_(30218, "location", lambda: location)] > _n_(30219, "nlist", lambda: nlist)[_n_(30220, "maxpos", lambda: maxpos)]:
                _l_(30223)

                maxpos = _n_(30221, "location", lambda: location)
                _l_(30222)
        temp = _n_(30225, "nlist", lambda: nlist)[_n_(30226, "fillslot", lambda: fillslot)]
        _l_(30227)
        _n_(30228, "nlist", lambda: nlist)[_n_(30229, "fillslot", lambda: fillslot)] = _n_(30230, "nlist", lambda: nlist)[_n_(30231, "maxpos", lambda: maxpos)]
        _l_(30232)
        _n_(30233, "nlist", lambda: nlist)[_n_(30234, "maxpos", lambda: maxpos)] = _n_(30235, "temp", lambda: temp)
        _l_(30236)
nlist = [14, 46, 43, 27, 57, 41, 45, 21, 70]
_l_(30239)
_c_(30242, _n_(30240, "selectionSort", lambda: selectionSort), _n_(30241, "nlist", lambda: nlist))
_l_(30243)
_c_(30246, _n_(30244, "print", lambda: print), _n_(30245, "nlist", lambda: nlist))
_l_(30247)