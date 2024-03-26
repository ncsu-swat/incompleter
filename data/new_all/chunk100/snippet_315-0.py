# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def selectionSort(nlist):
    _l_(110203)

    for fillslot in _c_(110177, _n_(110173, "range", lambda: range), _c_(110176, _n_(110174, "len", lambda: len), _n_(110175, "nlist", lambda: nlist)) - 1, 0, -1):
        _l_(110202)

        maxpos = 0
        _l_(110178)
        for location in _c_(110181, _n_(110179, "range", lambda: range), 1, _n_(110180, "fillslot", lambda: fillslot) + 1):
            _l_(110189)

            if _n_(110182, "nlist", lambda: nlist)[_n_(110183, "location", lambda: location)] > _n_(110184, "nlist", lambda: nlist)[_n_(110185, "maxpos", lambda: maxpos)]:
                _l_(110188)

                maxpos = _n_(110186, "location", lambda: location)
                _l_(110187)
        temp = _n_(110190, "nlist", lambda: nlist)[_n_(110191, "fillslot", lambda: fillslot)]
        _l_(110192)
        _n_(110193, "nlist", lambda: nlist)[_n_(110194, "fillslot", lambda: fillslot)] = _n_(110195, "nlist", lambda: nlist)[_n_(110196, "maxpos", lambda: maxpos)]
        _l_(110197)
        _n_(110198, "nlist", lambda: nlist)[_n_(110199, "maxpos", lambda: maxpos)] = _n_(110200, "temp", lambda: temp)
        _l_(110201)
_c_(110206, _n_(110204, "selectionSort", lambda: selectionSort), _n_(110205, "nlist", lambda: nlist))
_l_(110207)
_c_(110210, _n_(110208, "print", lambda: print), _n_(110209, "nlist", lambda: nlist))
_l_(110211)