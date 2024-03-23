# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def quickSort(data_list):
    _l_(76017)

    _c_(76015, _n_(76010, "quickSortHlp", lambda: quickSortHlp), _n_(76011, "data_list", lambda: data_list), 0, _c_(76014, _n_(76012, "len", lambda: len), _n_(76013, "data_list", lambda: data_list)) - 1)
    _l_(76016)

def quickSortHlp(data_list, first, last):
    _l_(76039)

    if _n_(76018, "first", lambda: first) < _n_(76019, "last", lambda: last):
        _l_(76038)

        splitpoint = _c_(76024, _n_(76020, "partition", lambda: partition), _n_(76021, "data_list", lambda: data_list), _n_(76022, "first", lambda: first), _n_(76023, "last", lambda: last))
        _l_(76025)
        _c_(76030, _n_(76026, "quickSortHlp", lambda: quickSortHlp), _n_(76027, "data_list", lambda: data_list), _n_(76028, "first", lambda: first), _n_(76029, "splitpoint", lambda: splitpoint) - 1)
        _l_(76031)
        _c_(76036, _n_(76032, "quickSortHlp", lambda: quickSortHlp), _n_(76033, "data_list", lambda: data_list), _n_(76034, "splitpoint", lambda: splitpoint) + 1, _n_(76035, "last", lambda: last))
        _l_(76037)

def partition(data_list, first, last):
    _l_(76094)

    pivotvalue = _n_(76040, "data_list", lambda: data_list)[_n_(76041, "first", lambda: first)]
    _l_(76042)
    rightmark = _n_(76043, "last", lambda: last)
    _l_(76044)
    done = False
    _l_(76045)
    while not _n_(76046, "done", lambda: done):
        _l_(76079)

        while _n_(76047, "leftmark", lambda: leftmark) <= _n_(76048, "rightmark", lambda: rightmark) and _n_(76049, "data_list", lambda: data_list)[_n_(76050, "leftmark", lambda: leftmark)] <= _n_(76051, "pivotvalue", lambda: pivotvalue):
            _l_(76054)

            leftmark = _n_(76052, "leftmark", lambda: leftmark) + 1
            _l_(76053)
        while _n_(76055, "data_list", lambda: data_list)[_n_(76056, "rightmark", lambda: rightmark)] >= _n_(76057, "pivotvalue", lambda: pivotvalue) and _n_(76058, "rightmark", lambda: rightmark) >= _n_(76059, "leftmark", lambda: leftmark):
            _l_(76062)

            rightmark = _n_(76060, "rightmark", lambda: rightmark) - 1
            _l_(76061)
        if _n_(76063, "rightmark", lambda: rightmark) < _n_(76064, "leftmark", lambda: leftmark):
            _l_(76078)

            done = True
            _l_(76065)
        else:
            temp = _n_(76066, "data_list", lambda: data_list)[_n_(76067, "leftmark", lambda: leftmark)]
            _l_(76068)
            _n_(76069, "data_list", lambda: data_list)[_n_(76070, "leftmark", lambda: leftmark)] = _n_(76071, "data_list", lambda: data_list)[_n_(76072, "rightmark", lambda: rightmark)]
            _l_(76073)
            _n_(76074, "data_list", lambda: data_list)[_n_(76075, "rightmark", lambda: rightmark)] = _n_(76076, "temp", lambda: temp)
            _l_(76077)
    temp = _n_(76080, "data_list", lambda: data_list)[_n_(76081, "first", lambda: first)]
    _l_(76082)
    _n_(76083, "data_list", lambda: data_list)[_n_(76084, "first", lambda: first)] = _n_(76085, "data_list", lambda: data_list)[_n_(76086, "rightmark", lambda: rightmark)]
    _l_(76087)
    _n_(76088, "data_list", lambda: data_list)[_n_(76089, "rightmark", lambda: rightmark)] = _n_(76090, "temp", lambda: temp)
    _l_(76091)
    aux = _n_(76092, "rightmark", lambda: rightmark)
    _l_(76093)
    return aux
data_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
_l_(76095)
_c_(76098, _n_(76096, "quickSort", lambda: quickSort), _n_(76097, "data_list", lambda: data_list))
_l_(76099)
_c_(76102, _n_(76100, "print", lambda: print), _n_(76101, "data_list", lambda: data_list))
_l_(76103)