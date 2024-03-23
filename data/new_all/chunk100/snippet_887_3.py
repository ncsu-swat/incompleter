# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def insertionSort(nlist):
    _l_(87280)

    for index in _c_(87259, _n_(87255, "range", lambda: range), 1, _c_(87258, _n_(87256, "len", lambda: len), _n_(87257, "nlist", lambda: nlist))):
        _l_(87279)

        currentvalue = _n_(87260, "nlist", lambda: nlist)[_n_(87261, "index", lambda: index)]
        _l_(87262)
        while _n_(87263, "position", lambda: position) > 0 and _n_(87264, "nlist", lambda: nlist)[_n_(87265, "position", lambda: position) - 1] > _n_(87266, "currentvalue", lambda: currentvalue):
            _l_(87274)

            _n_(87267, "nlist", lambda: nlist)[_n_(87268, "position", lambda: position)] = _n_(87269, "nlist", lambda: nlist)[_n_(87270, "position", lambda: position) - 1]
            _l_(87271)
            position = _n_(87272, "position", lambda: position) - 1
            _l_(87273)
        _n_(87275, "nlist", lambda: nlist)[_n_(87276, "position", lambda: position)] = _n_(87277, "currentvalue", lambda: currentvalue)
        _l_(87278)
nlist = [14, 46, 43, 27, 57, 41, 45, 21, 70]
_l_(87281)
_c_(87284, _n_(87282, "insertionSort", lambda: insertionSort), _n_(87283, "nlist", lambda: nlist))
_l_(87285)
_c_(87288, _n_(87286, "print", lambda: print), _n_(87287, "nlist", lambda: nlist))
_l_(87289)