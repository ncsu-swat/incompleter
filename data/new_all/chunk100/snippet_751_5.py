# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def quickSort(data_list):
    _l_(76301)

    _c_(76299, _n_(76294, "quickSortHlp", lambda: quickSortHlp), _n_(76295, "data_list", lambda: data_list), 0, _c_(76298, _n_(76296, "len", lambda: len), _n_(76297, "data_list", lambda: data_list)) - 1)
    _l_(76300)

def quickSortHlp(data_list, first, last):
    _l_(76323)

    if _n_(76302, "first", lambda: first) < _n_(76303, "last", lambda: last):
        _l_(76322)

        splitpoint = _c_(76308, _n_(76304, "partition", lambda: partition), _n_(76305, "data_list", lambda: data_list), _n_(76306, "first", lambda: first), _n_(76307, "last", lambda: last))
        _l_(76309)
        _c_(76314, _n_(76310, "quickSortHlp", lambda: quickSortHlp), _n_(76311, "data_list", lambda: data_list), _n_(76312, "first", lambda: first), _n_(76313, "splitpoint", lambda: splitpoint) - 1)
        _l_(76315)
        _c_(76320, _n_(76316, "quickSortHlp", lambda: quickSortHlp), _n_(76317, "data_list", lambda: data_list), _n_(76318, "splitpoint", lambda: splitpoint) + 1, _n_(76319, "last", lambda: last))
        _l_(76321)

def partition(data_list, first, last):
    _l_(76377)

    leftmark = _n_(76324, "first", lambda: first) + 1
    _l_(76325)
    rightmark = _n_(76326, "last", lambda: last)
    _l_(76327)
    done = False
    _l_(76328)
    while not _n_(76329, "done", lambda: done):
        _l_(76362)

        while _n_(76330, "leftmark", lambda: leftmark) <= _n_(76331, "rightmark", lambda: rightmark) and _n_(76332, "data_list", lambda: data_list)[_n_(76333, "leftmark", lambda: leftmark)] <= _n_(76334, "pivotvalue", lambda: pivotvalue):
            _l_(76337)

            leftmark = _n_(76335, "leftmark", lambda: leftmark) + 1
            _l_(76336)
        while _n_(76338, "data_list", lambda: data_list)[_n_(76339, "rightmark", lambda: rightmark)] >= _n_(76340, "pivotvalue", lambda: pivotvalue) and _n_(76341, "rightmark", lambda: rightmark) >= _n_(76342, "leftmark", lambda: leftmark):
            _l_(76345)

            rightmark = _n_(76343, "rightmark", lambda: rightmark) - 1
            _l_(76344)
        if _n_(76346, "rightmark", lambda: rightmark) < _n_(76347, "leftmark", lambda: leftmark):
            _l_(76361)

            done = True
            _l_(76348)
        else:
            temp = _n_(76349, "data_list", lambda: data_list)[_n_(76350, "leftmark", lambda: leftmark)]
            _l_(76351)
            _n_(76352, "data_list", lambda: data_list)[_n_(76353, "leftmark", lambda: leftmark)] = _n_(76354, "data_list", lambda: data_list)[_n_(76355, "rightmark", lambda: rightmark)]
            _l_(76356)
            _n_(76357, "data_list", lambda: data_list)[_n_(76358, "rightmark", lambda: rightmark)] = _n_(76359, "temp", lambda: temp)
            _l_(76360)
    temp = _n_(76363, "data_list", lambda: data_list)[_n_(76364, "first", lambda: first)]
    _l_(76365)
    _n_(76366, "data_list", lambda: data_list)[_n_(76367, "first", lambda: first)] = _n_(76368, "data_list", lambda: data_list)[_n_(76369, "rightmark", lambda: rightmark)]
    _l_(76370)
    _n_(76371, "data_list", lambda: data_list)[_n_(76372, "rightmark", lambda: rightmark)] = _n_(76373, "temp", lambda: temp)
    _l_(76374)
    aux = _n_(76375, "rightmark", lambda: rightmark)
    _l_(76376)
    return aux
data_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
_l_(76378)
_c_(76381, _n_(76379, "quickSort", lambda: quickSort), _n_(76380, "data_list", lambda: data_list))
_l_(76382)
_c_(76385, _n_(76383, "print", lambda: print), _n_(76384, "data_list", lambda: data_list))
_l_(76386)