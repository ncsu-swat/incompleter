# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def quickSort(data_list):
    _l_(76206)

    _c_(76204, _n_(76199, "quickSortHlp", lambda: quickSortHlp), _n_(76200, "data_list", lambda: data_list), 0, _c_(76203, _n_(76201, "len", lambda: len), _n_(76202, "data_list", lambda: data_list)) - 1)
    _l_(76205)

def quickSortHlp(data_list, first, last):
    _l_(76228)

    if _n_(76207, "first", lambda: first) < _n_(76208, "last", lambda: last):
        _l_(76227)

        splitpoint = _c_(76213, _n_(76209, "partition", lambda: partition), _n_(76210, "data_list", lambda: data_list), _n_(76211, "first", lambda: first), _n_(76212, "last", lambda: last))
        _l_(76214)
        _c_(76219, _n_(76215, "quickSortHlp", lambda: quickSortHlp), _n_(76216, "data_list", lambda: data_list), _n_(76217, "first", lambda: first), _n_(76218, "splitpoint", lambda: splitpoint) - 1)
        _l_(76220)
        _c_(76225, _n_(76221, "quickSortHlp", lambda: quickSortHlp), _n_(76222, "data_list", lambda: data_list), _n_(76223, "splitpoint", lambda: splitpoint) + 1, _n_(76224, "last", lambda: last))
        _l_(76226)

def partition(data_list, first, last):
    _l_(76285)

    pivotvalue = _n_(76229, "data_list", lambda: data_list)[_n_(76230, "first", lambda: first)]
    _l_(76231)
    leftmark = _n_(76232, "first", lambda: first) + 1
    _l_(76233)
    rightmark = _n_(76234, "last", lambda: last)
    _l_(76235)
    done = False
    _l_(76236)
    while not _n_(76237, "done", lambda: done):
        _l_(76270)

        while _n_(76238, "leftmark", lambda: leftmark) <= _n_(76239, "rightmark", lambda: rightmark) and _n_(76240, "data_list", lambda: data_list)[_n_(76241, "leftmark", lambda: leftmark)] <= _n_(76242, "pivotvalue", lambda: pivotvalue):
            _l_(76245)

            leftmark = _n_(76243, "leftmark", lambda: leftmark) + 1
            _l_(76244)
        while _n_(76246, "data_list", lambda: data_list)[_n_(76247, "rightmark", lambda: rightmark)] >= _n_(76248, "pivotvalue", lambda: pivotvalue) and _n_(76249, "rightmark", lambda: rightmark) >= _n_(76250, "leftmark", lambda: leftmark):
            _l_(76253)

            rightmark = _n_(76251, "rightmark", lambda: rightmark) - 1
            _l_(76252)
        if _n_(76254, "rightmark", lambda: rightmark) < _n_(76255, "leftmark", lambda: leftmark):
            _l_(76269)

            done = True
            _l_(76256)
        else:
            temp = _n_(76257, "data_list", lambda: data_list)[_n_(76258, "leftmark", lambda: leftmark)]
            _l_(76259)
            _n_(76260, "data_list", lambda: data_list)[_n_(76261, "leftmark", lambda: leftmark)] = _n_(76262, "data_list", lambda: data_list)[_n_(76263, "rightmark", lambda: rightmark)]
            _l_(76264)
            _n_(76265, "data_list", lambda: data_list)[_n_(76266, "rightmark", lambda: rightmark)] = _n_(76267, "temp", lambda: temp)
            _l_(76268)
    temp = _n_(76271, "data_list", lambda: data_list)[_n_(76272, "first", lambda: first)]
    _l_(76273)
    _n_(76274, "data_list", lambda: data_list)[_n_(76275, "first", lambda: first)] = _n_(76276, "data_list", lambda: data_list)[_n_(76277, "rightmark", lambda: rightmark)]
    _l_(76278)
    _n_(76279, "data_list", lambda: data_list)[_n_(76280, "rightmark", lambda: rightmark)] = _n_(76281, "temp", lambda: temp)
    _l_(76282)
    aux = _n_(76283, "rightmark", lambda: rightmark)
    _l_(76284)
    return aux
_c_(76288, _n_(76286, "quickSort", lambda: quickSort), _n_(76287, "data_list", lambda: data_list))
_l_(76289)
_c_(76292, _n_(76290, "print", lambda: print), _n_(76291, "data_list", lambda: data_list))
_l_(76293)