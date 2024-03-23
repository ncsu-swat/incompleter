# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def mergeSort(nlist):
    _l_(61852)

    _c_(61767, _n_(61765, "print", lambda: print), 'Splitting ', _n_(61766, "nlist", lambda: nlist))
    _l_(61768)
    if _c_(61771, _n_(61769, "len", lambda: len), _n_(61770, "nlist", lambda: nlist)) > 1:
        _l_(61847)

        mid = _c_(61774, _n_(61772, "len", lambda: len), _n_(61773, "nlist", lambda: nlist)) // 2
        _l_(61775)
        lefthalf = _n_(61776, "nlist", lambda: nlist)[:_n_(61777, "mid", lambda: mid)]
        _l_(61778)
        righthalf = _n_(61779, "nlist", lambda: nlist)[_n_(61780, "mid", lambda: mid):]
        _l_(61781)
        _c_(61784, _n_(61782, "mergeSort", lambda: mergeSort), _n_(61783, "lefthalf", lambda: lefthalf))
        _l_(61785)
        _c_(61788, _n_(61786, "mergeSort", lambda: mergeSort), _n_(61787, "righthalf", lambda: righthalf))
        _l_(61789)
        i = j = k = 0
        _l_(61790)
        while _n_(61791, "i", lambda: i) < _c_(61794, _n_(61792, "len", lambda: len), _n_(61793, "lefthalf", lambda: lefthalf)) and _n_(61795, "j", lambda: j) < _c_(61798, _n_(61796, "len", lambda: len), _n_(61797, "righthalf", lambda: righthalf)):
            _l_(61818)

            if _n_(61799, "lefthalf", lambda: lefthalf)[_n_(61800, "i", lambda: i)] < _n_(61801, "righthalf", lambda: righthalf)[_n_(61802, "j", lambda: j)]:
                _l_(61817)

                _n_(61803, "nlist", lambda: nlist)[_n_(61804, "k", lambda: k)] = _n_(61805, "lefthalf", lambda: lefthalf)[_n_(61806, "i", lambda: i)]
                _l_(61807)
                i = _n_(61808, "i", lambda: i) + 1
                _l_(61809)
            else:
                _n_(61810, "nlist", lambda: nlist)[_n_(61811, "k", lambda: k)] = _n_(61812, "righthalf", lambda: righthalf)[_n_(61813, "j", lambda: j)]
                _l_(61814)
                j = _n_(61815, "j", lambda: j) + 1
                _l_(61816)
        while _n_(61819, "i", lambda: i) < _c_(61822, _n_(61820, "len", lambda: len), _n_(61821, "lefthalf", lambda: lefthalf)):
            _l_(61832)

            _n_(61823, "nlist", lambda: nlist)[_n_(61824, "k", lambda: k)] = _n_(61825, "lefthalf", lambda: lefthalf)[_n_(61826, "i", lambda: i)]
            _l_(61827)
            i = _n_(61828, "i", lambda: i) + 1
            _l_(61829)
            k = _n_(61830, "k", lambda: k) + 1
            _l_(61831)
        while _n_(61833, "j", lambda: j) < _c_(61836, _n_(61834, "len", lambda: len), _n_(61835, "righthalf", lambda: righthalf)):
            _l_(61846)

            _n_(61837, "nlist", lambda: nlist)[_n_(61838, "k", lambda: k)] = _n_(61839, "righthalf", lambda: righthalf)[_n_(61840, "j", lambda: j)]
            _l_(61841)
            j = _n_(61842, "j", lambda: j) + 1
            _l_(61843)
            k = _n_(61844, "k", lambda: k) + 1
            _l_(61845)
    _c_(61850, _n_(61848, "print", lambda: print), 'Merging ', _n_(61849, "nlist", lambda: nlist))
    _l_(61851)
nlist = [14, 46, 43, 27, 57, 41, 45, 21, 70]
_l_(61853)
_c_(61856, _n_(61854, "mergeSort", lambda: mergeSort), _n_(61855, "nlist", lambda: nlist))
_l_(61857)
_c_(61860, _n_(61858, "print", lambda: print), _n_(61859, "nlist", lambda: nlist))
_l_(61861)