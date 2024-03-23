# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def quickSort(data_list):
    _l_(75923)

    _c_(75921, _n_(75916, "quickSortHlp", lambda: quickSortHlp), _n_(75917, "data_list", lambda: data_list), 0, _c_(75920, _n_(75918, "len", lambda: len), _n_(75919, "data_list", lambda: data_list)) - 1)
    _l_(75922)

def quickSortHlp(data_list, first, last):
    _l_(75945)

    if _n_(75924, "first", lambda: first) < _n_(75925, "last", lambda: last):
        _l_(75944)

        splitpoint = _c_(75930, _n_(75926, "partition", lambda: partition), _n_(75927, "data_list", lambda: data_list), _n_(75928, "first", lambda: first), _n_(75929, "last", lambda: last))
        _l_(75931)
        _c_(75936, _n_(75932, "quickSortHlp", lambda: quickSortHlp), _n_(75933, "data_list", lambda: data_list), _n_(75934, "first", lambda: first), _n_(75935, "splitpoint", lambda: splitpoint) - 1)
        _l_(75937)
        _c_(75942, _n_(75938, "quickSortHlp", lambda: quickSortHlp), _n_(75939, "data_list", lambda: data_list), _n_(75940, "splitpoint", lambda: splitpoint) + 1, _n_(75941, "last", lambda: last))
        _l_(75943)

def partition(data_list, first, last):
    _l_(76000)

    pivotvalue = _n_(75946, "data_list", lambda: data_list)[_n_(75947, "first", lambda: first)]
    _l_(75948)
    leftmark = _n_(75949, "first", lambda: first) + 1
    _l_(75950)
    done = False
    _l_(75951)
    while not _n_(75952, "done", lambda: done):
        _l_(75985)

        while _n_(75953, "leftmark", lambda: leftmark) <= _n_(75954, "rightmark", lambda: rightmark) and _n_(75955, "data_list", lambda: data_list)[_n_(75956, "leftmark", lambda: leftmark)] <= _n_(75957, "pivotvalue", lambda: pivotvalue):
            _l_(75960)

            leftmark = _n_(75958, "leftmark", lambda: leftmark) + 1
            _l_(75959)
        while _n_(75961, "data_list", lambda: data_list)[_n_(75962, "rightmark", lambda: rightmark)] >= _n_(75963, "pivotvalue", lambda: pivotvalue) and _n_(75964, "rightmark", lambda: rightmark) >= _n_(75965, "leftmark", lambda: leftmark):
            _l_(75968)

            rightmark = _n_(75966, "rightmark", lambda: rightmark) - 1
            _l_(75967)
        if _n_(75969, "rightmark", lambda: rightmark) < _n_(75970, "leftmark", lambda: leftmark):
            _l_(75984)

            done = True
            _l_(75971)
        else:
            temp = _n_(75972, "data_list", lambda: data_list)[_n_(75973, "leftmark", lambda: leftmark)]
            _l_(75974)
            _n_(75975, "data_list", lambda: data_list)[_n_(75976, "leftmark", lambda: leftmark)] = _n_(75977, "data_list", lambda: data_list)[_n_(75978, "rightmark", lambda: rightmark)]
            _l_(75979)
            _n_(75980, "data_list", lambda: data_list)[_n_(75981, "rightmark", lambda: rightmark)] = _n_(75982, "temp", lambda: temp)
            _l_(75983)
    temp = _n_(75986, "data_list", lambda: data_list)[_n_(75987, "first", lambda: first)]
    _l_(75988)
    _n_(75989, "data_list", lambda: data_list)[_n_(75990, "first", lambda: first)] = _n_(75991, "data_list", lambda: data_list)[_n_(75992, "rightmark", lambda: rightmark)]
    _l_(75993)
    _n_(75994, "data_list", lambda: data_list)[_n_(75995, "rightmark", lambda: rightmark)] = _n_(75996, "temp", lambda: temp)
    _l_(75997)
    aux = _n_(75998, "rightmark", lambda: rightmark)
    _l_(75999)
    return aux
data_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
_l_(76001)
_c_(76004, _n_(76002, "quickSort", lambda: quickSort), _n_(76003, "data_list", lambda: data_list))
_l_(76005)
_c_(76008, _n_(76006, "print", lambda: print), _n_(76007, "data_list", lambda: data_list))
_l_(76009)