# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def mergeSort(nlist):
    _l_(62240)

    _c_(62156, _n_(62154, "print", lambda: print), 'Splitting ', _n_(62155, "nlist", lambda: nlist))
    _l_(62157)
    if _c_(62160, _n_(62158, "len", lambda: len), _n_(62159, "nlist", lambda: nlist)) > 1:
        _l_(62235)

        mid = _c_(62163, _n_(62161, "len", lambda: len), _n_(62162, "nlist", lambda: nlist)) // 2
        _l_(62164)
        lefthalf = _n_(62165, "nlist", lambda: nlist)[:_n_(62166, "mid", lambda: mid)]
        _l_(62167)
        _c_(62170, _n_(62168, "mergeSort", lambda: mergeSort), _n_(62169, "lefthalf", lambda: lefthalf))
        _l_(62171)
        _c_(62174, _n_(62172, "mergeSort", lambda: mergeSort), _n_(62173, "righthalf", lambda: righthalf))
        _l_(62175)
        i = j = k = 0
        _l_(62176)
        while _n_(62177, "i", lambda: i) < _c_(62180, _n_(62178, "len", lambda: len), _n_(62179, "lefthalf", lambda: lefthalf)) and _n_(62181, "j", lambda: j) < _c_(62184, _n_(62182, "len", lambda: len), _n_(62183, "righthalf", lambda: righthalf)):
            _l_(62206)

            if _n_(62185, "lefthalf", lambda: lefthalf)[_n_(62186, "i", lambda: i)] < _n_(62187, "righthalf", lambda: righthalf)[_n_(62188, "j", lambda: j)]:
                _l_(62203)

                _n_(62189, "nlist", lambda: nlist)[_n_(62190, "k", lambda: k)] = _n_(62191, "lefthalf", lambda: lefthalf)[_n_(62192, "i", lambda: i)]
                _l_(62193)
                i = _n_(62194, "i", lambda: i) + 1
                _l_(62195)
            else:
                _n_(62196, "nlist", lambda: nlist)[_n_(62197, "k", lambda: k)] = _n_(62198, "righthalf", lambda: righthalf)[_n_(62199, "j", lambda: j)]
                _l_(62200)
                j = _n_(62201, "j", lambda: j) + 1
                _l_(62202)
            k = _n_(62204, "k", lambda: k) + 1
            _l_(62205)
        while _n_(62207, "i", lambda: i) < _c_(62210, _n_(62208, "len", lambda: len), _n_(62209, "lefthalf", lambda: lefthalf)):
            _l_(62220)

            _n_(62211, "nlist", lambda: nlist)[_n_(62212, "k", lambda: k)] = _n_(62213, "lefthalf", lambda: lefthalf)[_n_(62214, "i", lambda: i)]
            _l_(62215)
            i = _n_(62216, "i", lambda: i) + 1
            _l_(62217)
            k = _n_(62218, "k", lambda: k) + 1
            _l_(62219)
        while _n_(62221, "j", lambda: j) < _c_(62224, _n_(62222, "len", lambda: len), _n_(62223, "righthalf", lambda: righthalf)):
            _l_(62234)

            _n_(62225, "nlist", lambda: nlist)[_n_(62226, "k", lambda: k)] = _n_(62227, "righthalf", lambda: righthalf)[_n_(62228, "j", lambda: j)]
            _l_(62229)
            j = _n_(62230, "j", lambda: j) + 1
            _l_(62231)
            k = _n_(62232, "k", lambda: k) + 1
            _l_(62233)
    _c_(62238, _n_(62236, "print", lambda: print), 'Merging ', _n_(62237, "nlist", lambda: nlist))
    _l_(62239)
nlist = [14, 46, 43, 27, 57, 41, 45, 21, 70]
_l_(62241)
_c_(62244, _n_(62242, "mergeSort", lambda: mergeSort), _n_(62243, "nlist", lambda: nlist))
_l_(62245)
_c_(62248, _n_(62246, "print", lambda: print), _n_(62247, "nlist", lambda: nlist))
_l_(62249)