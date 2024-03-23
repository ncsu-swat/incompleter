# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def mergeSort(nlist):
    _l_(62432)

    _c_(62349, _n_(62347, "print", lambda: print), 'Splitting ', _n_(62348, "nlist", lambda: nlist))
    _l_(62350)
    if _c_(62353, _n_(62351, "len", lambda: len), _n_(62352, "nlist", lambda: nlist)) > 1:
        _l_(62427)

        lefthalf = _n_(62354, "nlist", lambda: nlist)[:_n_(62355, "mid", lambda: mid)]
        _l_(62356)
        righthalf = _n_(62357, "nlist", lambda: nlist)[_n_(62358, "mid", lambda: mid):]
        _l_(62359)
        _c_(62362, _n_(62360, "mergeSort", lambda: mergeSort), _n_(62361, "lefthalf", lambda: lefthalf))
        _l_(62363)
        _c_(62366, _n_(62364, "mergeSort", lambda: mergeSort), _n_(62365, "righthalf", lambda: righthalf))
        _l_(62367)
        i = j = k = 0
        _l_(62368)
        while _n_(62369, "i", lambda: i) < _c_(62372, _n_(62370, "len", lambda: len), _n_(62371, "lefthalf", lambda: lefthalf)) and _n_(62373, "j", lambda: j) < _c_(62376, _n_(62374, "len", lambda: len), _n_(62375, "righthalf", lambda: righthalf)):
            _l_(62398)

            if _n_(62377, "lefthalf", lambda: lefthalf)[_n_(62378, "i", lambda: i)] < _n_(62379, "righthalf", lambda: righthalf)[_n_(62380, "j", lambda: j)]:
                _l_(62395)

                _n_(62381, "nlist", lambda: nlist)[_n_(62382, "k", lambda: k)] = _n_(62383, "lefthalf", lambda: lefthalf)[_n_(62384, "i", lambda: i)]
                _l_(62385)
                i = _n_(62386, "i", lambda: i) + 1
                _l_(62387)
            else:
                _n_(62388, "nlist", lambda: nlist)[_n_(62389, "k", lambda: k)] = _n_(62390, "righthalf", lambda: righthalf)[_n_(62391, "j", lambda: j)]
                _l_(62392)
                j = _n_(62393, "j", lambda: j) + 1
                _l_(62394)
            k = _n_(62396, "k", lambda: k) + 1
            _l_(62397)
        while _n_(62399, "i", lambda: i) < _c_(62402, _n_(62400, "len", lambda: len), _n_(62401, "lefthalf", lambda: lefthalf)):
            _l_(62412)

            _n_(62403, "nlist", lambda: nlist)[_n_(62404, "k", lambda: k)] = _n_(62405, "lefthalf", lambda: lefthalf)[_n_(62406, "i", lambda: i)]
            _l_(62407)
            i = _n_(62408, "i", lambda: i) + 1
            _l_(62409)
            k = _n_(62410, "k", lambda: k) + 1
            _l_(62411)
        while _n_(62413, "j", lambda: j) < _c_(62416, _n_(62414, "len", lambda: len), _n_(62415, "righthalf", lambda: righthalf)):
            _l_(62426)

            _n_(62417, "nlist", lambda: nlist)[_n_(62418, "k", lambda: k)] = _n_(62419, "righthalf", lambda: righthalf)[_n_(62420, "j", lambda: j)]
            _l_(62421)
            j = _n_(62422, "j", lambda: j) + 1
            _l_(62423)
            k = _n_(62424, "k", lambda: k) + 1
            _l_(62425)
    _c_(62430, _n_(62428, "print", lambda: print), 'Merging ', _n_(62429, "nlist", lambda: nlist))
    _l_(62431)
nlist = [14, 46, 43, 27, 57, 41, 45, 21, 70]
_l_(62433)
_c_(62436, _n_(62434, "mergeSort", lambda: mergeSort), _n_(62435, "nlist", lambda: nlist))
_l_(62437)
_c_(62440, _n_(62438, "print", lambda: print), _n_(62439, "nlist", lambda: nlist))
_l_(62441)