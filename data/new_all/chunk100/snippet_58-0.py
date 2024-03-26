# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def mergeSort(nlist):
    _l_(119389)

    _c_(119302, _n_(119300, "print", lambda: print), 'Splitting ', _n_(119301, "nlist", lambda: nlist))
    _l_(119303)
    if _c_(119306, _n_(119304, "len", lambda: len), _n_(119305, "nlist", lambda: nlist)) > 1:
        _l_(119384)

        mid = _c_(119309, _n_(119307, "len", lambda: len), _n_(119308, "nlist", lambda: nlist)) // 2
        _l_(119310)
        lefthalf = _n_(119311, "nlist", lambda: nlist)[:_n_(119312, "mid", lambda: mid)]
        _l_(119313)
        righthalf = _n_(119314, "nlist", lambda: nlist)[_n_(119315, "mid", lambda: mid):]
        _l_(119316)
        _c_(119319, _n_(119317, "mergeSort", lambda: mergeSort), _n_(119318, "lefthalf", lambda: lefthalf))
        _l_(119320)
        _c_(119323, _n_(119321, "mergeSort", lambda: mergeSort), _n_(119322, "righthalf", lambda: righthalf))
        _l_(119324)
        i = j = k = 0
        _l_(119325)
        while _n_(119326, "i", lambda: i) < _c_(119329, _n_(119327, "len", lambda: len), _n_(119328, "lefthalf", lambda: lefthalf)) and _n_(119330, "j", lambda: j) < _c_(119333, _n_(119331, "len", lambda: len), _n_(119332, "righthalf", lambda: righthalf)):
            _l_(119355)

            if _n_(119334, "lefthalf", lambda: lefthalf)[_n_(119335, "i", lambda: i)] < _n_(119336, "righthalf", lambda: righthalf)[_n_(119337, "j", lambda: j)]:
                _l_(119352)

                _n_(119338, "nlist", lambda: nlist)[_n_(119339, "k", lambda: k)] = _n_(119340, "lefthalf", lambda: lefthalf)[_n_(119341, "i", lambda: i)]
                _l_(119342)
                i = _n_(119343, "i", lambda: i) + 1
                _l_(119344)
            else:
                _n_(119345, "nlist", lambda: nlist)[_n_(119346, "k", lambda: k)] = _n_(119347, "righthalf", lambda: righthalf)[_n_(119348, "j", lambda: j)]
                _l_(119349)
                j = _n_(119350, "j", lambda: j) + 1
                _l_(119351)
            k = _n_(119353, "k", lambda: k) + 1
            _l_(119354)
        while _n_(119356, "i", lambda: i) < _c_(119359, _n_(119357, "len", lambda: len), _n_(119358, "lefthalf", lambda: lefthalf)):
            _l_(119369)

            _n_(119360, "nlist", lambda: nlist)[_n_(119361, "k", lambda: k)] = _n_(119362, "lefthalf", lambda: lefthalf)[_n_(119363, "i", lambda: i)]
            _l_(119364)
            i = _n_(119365, "i", lambda: i) + 1
            _l_(119366)
            k = _n_(119367, "k", lambda: k) + 1
            _l_(119368)
        while _n_(119370, "j", lambda: j) < _c_(119373, _n_(119371, "len", lambda: len), _n_(119372, "righthalf", lambda: righthalf)):
            _l_(119383)

            _n_(119374, "nlist", lambda: nlist)[_n_(119375, "k", lambda: k)] = _n_(119376, "righthalf", lambda: righthalf)[_n_(119377, "j", lambda: j)]
            _l_(119378)
            j = _n_(119379, "j", lambda: j) + 1
            _l_(119380)
            k = _n_(119381, "k", lambda: k) + 1
            _l_(119382)
    _c_(119387, _n_(119385, "print", lambda: print), 'Merging ', _n_(119386, "nlist", lambda: nlist))
    _l_(119388)
_c_(119392, _n_(119390, "mergeSort", lambda: mergeSort), _n_(119391, "nlist", lambda: nlist))
_l_(119393)
_c_(119396, _n_(119394, "print", lambda: print), _n_(119395, "nlist", lambda: nlist))
_l_(119397)