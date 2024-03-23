# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def mergeSort(nlist):
    _l_(62337)

    _c_(62252, _n_(62250, "print", lambda: print), 'Splitting ', _n_(62251, "nlist", lambda: nlist))
    _l_(62253)
    if _c_(62256, _n_(62254, "len", lambda: len), _n_(62255, "nlist", lambda: nlist)) > 1:
        _l_(62332)

        mid = _c_(62259, _n_(62257, "len", lambda: len), _n_(62258, "nlist", lambda: nlist)) // 2
        _l_(62260)
        lefthalf = _n_(62261, "nlist", lambda: nlist)[:_n_(62262, "mid", lambda: mid)]
        _l_(62263)
        righthalf = _n_(62264, "nlist", lambda: nlist)[_n_(62265, "mid", lambda: mid):]
        _l_(62266)
        _c_(62269, _n_(62267, "mergeSort", lambda: mergeSort), _n_(62268, "lefthalf", lambda: lefthalf))
        _l_(62270)
        _c_(62273, _n_(62271, "mergeSort", lambda: mergeSort), _n_(62272, "righthalf", lambda: righthalf))
        _l_(62274)
        i = j = k = 0
        _l_(62275)
        while _n_(62276, "i", lambda: i) < _c_(62279, _n_(62277, "len", lambda: len), _n_(62278, "lefthalf", lambda: lefthalf)) and _n_(62280, "j", lambda: j) < _c_(62283, _n_(62281, "len", lambda: len), _n_(62282, "righthalf", lambda: righthalf)):
            _l_(62303)

            if _n_(62284, "lefthalf", lambda: lefthalf)[_n_(62285, "i", lambda: i)] < _n_(62286, "righthalf", lambda: righthalf)[_n_(62287, "j", lambda: j)]:
                _l_(62300)

                _n_(62288, "nlist", lambda: nlist)[_n_(62289, "k", lambda: k)] = _n_(62290, "lefthalf", lambda: lefthalf)[_n_(62291, "i", lambda: i)]
                _l_(62292)
            else:
                _n_(62293, "nlist", lambda: nlist)[_n_(62294, "k", lambda: k)] = _n_(62295, "righthalf", lambda: righthalf)[_n_(62296, "j", lambda: j)]
                _l_(62297)
                j = _n_(62298, "j", lambda: j) + 1
                _l_(62299)
            k = _n_(62301, "k", lambda: k) + 1
            _l_(62302)
        while _n_(62304, "i", lambda: i) < _c_(62307, _n_(62305, "len", lambda: len), _n_(62306, "lefthalf", lambda: lefthalf)):
            _l_(62317)

            _n_(62308, "nlist", lambda: nlist)[_n_(62309, "k", lambda: k)] = _n_(62310, "lefthalf", lambda: lefthalf)[_n_(62311, "i", lambda: i)]
            _l_(62312)
            i = _n_(62313, "i", lambda: i) + 1
            _l_(62314)
            k = _n_(62315, "k", lambda: k) + 1
            _l_(62316)
        while _n_(62318, "j", lambda: j) < _c_(62321, _n_(62319, "len", lambda: len), _n_(62320, "righthalf", lambda: righthalf)):
            _l_(62331)

            _n_(62322, "nlist", lambda: nlist)[_n_(62323, "k", lambda: k)] = _n_(62324, "righthalf", lambda: righthalf)[_n_(62325, "j", lambda: j)]
            _l_(62326)
            j = _n_(62327, "j", lambda: j) + 1
            _l_(62328)
            k = _n_(62329, "k", lambda: k) + 1
            _l_(62330)
    _c_(62335, _n_(62333, "print", lambda: print), 'Merging ', _n_(62334, "nlist", lambda: nlist))
    _l_(62336)
nlist = [14, 46, 43, 27, 57, 41, 45, 21, 70]
_l_(62338)
_c_(62341, _n_(62339, "mergeSort", lambda: mergeSort), _n_(62340, "nlist", lambda: nlist))
_l_(62342)
_c_(62345, _n_(62343, "print", lambda: print), _n_(62344, "nlist", lambda: nlist))
_l_(62346)