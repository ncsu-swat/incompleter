# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def quickSort(data_list):
    _l_(76484)

    _c_(76482, _n_(76477, "quickSortHlp", lambda: quickSortHlp), _n_(76478, "data_list", lambda: data_list), 0, _c_(76481, _n_(76479, "len", lambda: len), _n_(76480, "data_list", lambda: data_list)) - 1)
    _l_(76483)

def quickSortHlp(data_list, first, last):
    _l_(76506)

    if _n_(76485, "first", lambda: first) < _n_(76486, "last", lambda: last):
        _l_(76505)

        splitpoint = _c_(76491, _n_(76487, "partition", lambda: partition), _n_(76488, "data_list", lambda: data_list), _n_(76489, "first", lambda: first), _n_(76490, "last", lambda: last))
        _l_(76492)
        _c_(76497, _n_(76493, "quickSortHlp", lambda: quickSortHlp), _n_(76494, "data_list", lambda: data_list), _n_(76495, "first", lambda: first), _n_(76496, "splitpoint", lambda: splitpoint) - 1)
        _l_(76498)
        _c_(76503, _n_(76499, "quickSortHlp", lambda: quickSortHlp), _n_(76500, "data_list", lambda: data_list), _n_(76501, "splitpoint", lambda: splitpoint) + 1, _n_(76502, "last", lambda: last))
        _l_(76504)

def partition(data_list, first, last):
    _l_(76560)

    pivotvalue = _n_(76507, "data_list", lambda: data_list)[_n_(76508, "first", lambda: first)]
    _l_(76509)
    leftmark = _n_(76510, "first", lambda: first) + 1
    _l_(76511)
    rightmark = _n_(76512, "last", lambda: last)
    _l_(76513)
    done = False
    _l_(76514)
    while not _n_(76515, "done", lambda: done):
        _l_(76548)

        while _n_(76516, "leftmark", lambda: leftmark) <= _n_(76517, "rightmark", lambda: rightmark) and _n_(76518, "data_list", lambda: data_list)[_n_(76519, "leftmark", lambda: leftmark)] <= _n_(76520, "pivotvalue", lambda: pivotvalue):
            _l_(76523)

            leftmark = _n_(76521, "leftmark", lambda: leftmark) + 1
            _l_(76522)
        while _n_(76524, "data_list", lambda: data_list)[_n_(76525, "rightmark", lambda: rightmark)] >= _n_(76526, "pivotvalue", lambda: pivotvalue) and _n_(76527, "rightmark", lambda: rightmark) >= _n_(76528, "leftmark", lambda: leftmark):
            _l_(76531)

            rightmark = _n_(76529, "rightmark", lambda: rightmark) - 1
            _l_(76530)
        if _n_(76532, "rightmark", lambda: rightmark) < _n_(76533, "leftmark", lambda: leftmark):
            _l_(76547)

            done = True
            _l_(76534)
        else:
            temp = _n_(76535, "data_list", lambda: data_list)[_n_(76536, "leftmark", lambda: leftmark)]
            _l_(76537)
            _n_(76538, "data_list", lambda: data_list)[_n_(76539, "leftmark", lambda: leftmark)] = _n_(76540, "data_list", lambda: data_list)[_n_(76541, "rightmark", lambda: rightmark)]
            _l_(76542)
            _n_(76543, "data_list", lambda: data_list)[_n_(76544, "rightmark", lambda: rightmark)] = _n_(76545, "temp", lambda: temp)
            _l_(76546)
    _n_(76549, "data_list", lambda: data_list)[_n_(76550, "first", lambda: first)] = _n_(76551, "data_list", lambda: data_list)[_n_(76552, "rightmark", lambda: rightmark)]
    _l_(76553)
    _n_(76554, "data_list", lambda: data_list)[_n_(76555, "rightmark", lambda: rightmark)] = _n_(76556, "temp", lambda: temp)
    _l_(76557)
    aux = _n_(76558, "rightmark", lambda: rightmark)
    _l_(76559)
    return aux
data_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
_l_(76561)
_c_(76564, _n_(76562, "quickSort", lambda: quickSort), _n_(76563, "data_list", lambda: data_list))
_l_(76565)
_c_(76568, _n_(76566, "print", lambda: print), _n_(76567, "data_list", lambda: data_list))
_l_(76569)