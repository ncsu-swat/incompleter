# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def quickSort(data_list):
    _l_(76394)

    _c_(76392, _n_(76387, "quickSortHlp", lambda: quickSortHlp), _n_(76388, "data_list", lambda: data_list), 0, _c_(76391, _n_(76389, "len", lambda: len), _n_(76390, "data_list", lambda: data_list)) - 1)
    _l_(76393)

def quickSortHlp(data_list, first, last):
    _l_(76410)

    if _n_(76395, "first", lambda: first) < _n_(76396, "last", lambda: last):
        _l_(76409)

        _c_(76401, _n_(76397, "quickSortHlp", lambda: quickSortHlp), _n_(76398, "data_list", lambda: data_list), _n_(76399, "first", lambda: first), _n_(76400, "splitpoint", lambda: splitpoint) - 1)
        _l_(76402)
        _c_(76407, _n_(76403, "quickSortHlp", lambda: quickSortHlp), _n_(76404, "data_list", lambda: data_list), _n_(76405, "splitpoint", lambda: splitpoint) + 1, _n_(76406, "last", lambda: last))
        _l_(76408)

def partition(data_list, first, last):
    _l_(76467)

    pivotvalue = _n_(76411, "data_list", lambda: data_list)[_n_(76412, "first", lambda: first)]
    _l_(76413)
    leftmark = _n_(76414, "first", lambda: first) + 1
    _l_(76415)
    rightmark = _n_(76416, "last", lambda: last)
    _l_(76417)
    done = False
    _l_(76418)
    while not _n_(76419, "done", lambda: done):
        _l_(76452)

        while _n_(76420, "leftmark", lambda: leftmark) <= _n_(76421, "rightmark", lambda: rightmark) and _n_(76422, "data_list", lambda: data_list)[_n_(76423, "leftmark", lambda: leftmark)] <= _n_(76424, "pivotvalue", lambda: pivotvalue):
            _l_(76427)

            leftmark = _n_(76425, "leftmark", lambda: leftmark) + 1
            _l_(76426)
        while _n_(76428, "data_list", lambda: data_list)[_n_(76429, "rightmark", lambda: rightmark)] >= _n_(76430, "pivotvalue", lambda: pivotvalue) and _n_(76431, "rightmark", lambda: rightmark) >= _n_(76432, "leftmark", lambda: leftmark):
            _l_(76435)

            rightmark = _n_(76433, "rightmark", lambda: rightmark) - 1
            _l_(76434)
        if _n_(76436, "rightmark", lambda: rightmark) < _n_(76437, "leftmark", lambda: leftmark):
            _l_(76451)

            done = True
            _l_(76438)
        else:
            temp = _n_(76439, "data_list", lambda: data_list)[_n_(76440, "leftmark", lambda: leftmark)]
            _l_(76441)
            _n_(76442, "data_list", lambda: data_list)[_n_(76443, "leftmark", lambda: leftmark)] = _n_(76444, "data_list", lambda: data_list)[_n_(76445, "rightmark", lambda: rightmark)]
            _l_(76446)
            _n_(76447, "data_list", lambda: data_list)[_n_(76448, "rightmark", lambda: rightmark)] = _n_(76449, "temp", lambda: temp)
            _l_(76450)
    temp = _n_(76453, "data_list", lambda: data_list)[_n_(76454, "first", lambda: first)]
    _l_(76455)
    _n_(76456, "data_list", lambda: data_list)[_n_(76457, "first", lambda: first)] = _n_(76458, "data_list", lambda: data_list)[_n_(76459, "rightmark", lambda: rightmark)]
    _l_(76460)
    _n_(76461, "data_list", lambda: data_list)[_n_(76462, "rightmark", lambda: rightmark)] = _n_(76463, "temp", lambda: temp)
    _l_(76464)
    aux = _n_(76465, "rightmark", lambda: rightmark)
    _l_(76466)
    return aux
data_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
_l_(76468)
_c_(76471, _n_(76469, "quickSort", lambda: quickSort), _n_(76470, "data_list", lambda: data_list))
_l_(76472)
_c_(76475, _n_(76473, "print", lambda: print), _n_(76474, "data_list", lambda: data_list))
_l_(76476)