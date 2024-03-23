# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def selectionSort(nlist):
    _l_(30160)

    for fillslot in _c_(30137, _n_(30133, "range", lambda: range), _c_(30136, _n_(30134, "len", lambda: len), _n_(30135, "nlist", lambda: nlist)) - 1, 0, -1):
        _l_(30159)

        maxpos = 0
        _l_(30138)
        for location in _c_(30141, _n_(30139, "range", lambda: range), 1, _n_(30140, "fillslot", lambda: fillslot) + 1):
            _l_(30149)

            if _n_(30142, "nlist", lambda: nlist)[_n_(30143, "location", lambda: location)] > _n_(30144, "nlist", lambda: nlist)[_n_(30145, "maxpos", lambda: maxpos)]:
                _l_(30148)

                maxpos = _n_(30146, "location", lambda: location)
                _l_(30147)
        _n_(30150, "nlist", lambda: nlist)[_n_(30151, "fillslot", lambda: fillslot)] = _n_(30152, "nlist", lambda: nlist)[_n_(30153, "maxpos", lambda: maxpos)]
        _l_(30154)
        _n_(30155, "nlist", lambda: nlist)[_n_(30156, "maxpos", lambda: maxpos)] = _n_(30157, "temp", lambda: temp)
        _l_(30158)
nlist = [14, 46, 43, 27, 57, 41, 45, 21, 70]
_l_(30161)
_c_(30164, _n_(30162, "selectionSort", lambda: selectionSort), _n_(30163, "nlist", lambda: nlist))
_l_(30165)
_c_(30168, _n_(30166, "print", lambda: print), _n_(30167, "nlist", lambda: nlist))
_l_(30169)