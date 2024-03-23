# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def quickSort(data_list):
    _l_(76111)

    _c_(76109, _n_(76104, "quickSortHlp", lambda: quickSortHlp), _n_(76105, "data_list", lambda: data_list), 0, _c_(76108, _n_(76106, "len", lambda: len), _n_(76107, "data_list", lambda: data_list)) - 1)
    _l_(76110)

def quickSortHlp(data_list, first, last):
    _l_(76133)

    if _n_(76112, "first", lambda: first) < _n_(76113, "last", lambda: last):
        _l_(76132)

        splitpoint = _c_(76118, _n_(76114, "partition", lambda: partition), _n_(76115, "data_list", lambda: data_list), _n_(76116, "first", lambda: first), _n_(76117, "last", lambda: last))
        _l_(76119)
        _c_(76124, _n_(76120, "quickSortHlp", lambda: quickSortHlp), _n_(76121, "data_list", lambda: data_list), _n_(76122, "first", lambda: first), _n_(76123, "splitpoint", lambda: splitpoint) - 1)
        _l_(76125)
        _c_(76130, _n_(76126, "quickSortHlp", lambda: quickSortHlp), _n_(76127, "data_list", lambda: data_list), _n_(76128, "splitpoint", lambda: splitpoint) + 1, _n_(76129, "last", lambda: last))
        _l_(76131)

def partition(data_list, first, last):
    _l_(76189)

    pivotvalue = _n_(76134, "data_list", lambda: data_list)[_n_(76135, "first", lambda: first)]
    _l_(76136)
    leftmark = _n_(76137, "first", lambda: first) + 1
    _l_(76138)
    rightmark = _n_(76139, "last", lambda: last)
    _l_(76140)
    while not _n_(76141, "done", lambda: done):
        _l_(76174)

        while _n_(76142, "leftmark", lambda: leftmark) <= _n_(76143, "rightmark", lambda: rightmark) and _n_(76144, "data_list", lambda: data_list)[_n_(76145, "leftmark", lambda: leftmark)] <= _n_(76146, "pivotvalue", lambda: pivotvalue):
            _l_(76149)

            leftmark = _n_(76147, "leftmark", lambda: leftmark) + 1
            _l_(76148)
        while _n_(76150, "data_list", lambda: data_list)[_n_(76151, "rightmark", lambda: rightmark)] >= _n_(76152, "pivotvalue", lambda: pivotvalue) and _n_(76153, "rightmark", lambda: rightmark) >= _n_(76154, "leftmark", lambda: leftmark):
            _l_(76157)

            rightmark = _n_(76155, "rightmark", lambda: rightmark) - 1
            _l_(76156)
        if _n_(76158, "rightmark", lambda: rightmark) < _n_(76159, "leftmark", lambda: leftmark):
            _l_(76173)

            done = True
            _l_(76160)
        else:
            temp = _n_(76161, "data_list", lambda: data_list)[_n_(76162, "leftmark", lambda: leftmark)]
            _l_(76163)
            _n_(76164, "data_list", lambda: data_list)[_n_(76165, "leftmark", lambda: leftmark)] = _n_(76166, "data_list", lambda: data_list)[_n_(76167, "rightmark", lambda: rightmark)]
            _l_(76168)
            _n_(76169, "data_list", lambda: data_list)[_n_(76170, "rightmark", lambda: rightmark)] = _n_(76171, "temp", lambda: temp)
            _l_(76172)
    temp = _n_(76175, "data_list", lambda: data_list)[_n_(76176, "first", lambda: first)]
    _l_(76177)
    _n_(76178, "data_list", lambda: data_list)[_n_(76179, "first", lambda: first)] = _n_(76180, "data_list", lambda: data_list)[_n_(76181, "rightmark", lambda: rightmark)]
    _l_(76182)
    _n_(76183, "data_list", lambda: data_list)[_n_(76184, "rightmark", lambda: rightmark)] = _n_(76185, "temp", lambda: temp)
    _l_(76186)
    aux = _n_(76187, "rightmark", lambda: rightmark)
    _l_(76188)
    return aux
data_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
_l_(76190)
_c_(76193, _n_(76191, "quickSort", lambda: quickSort), _n_(76192, "data_list", lambda: data_list))
_l_(76194)
_c_(76197, _n_(76195, "print", lambda: print), _n_(76196, "data_list", lambda: data_list))
_l_(76198)