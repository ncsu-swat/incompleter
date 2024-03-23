# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def mergeSort(nlist):
    _l_(61949)

    _c_(61864, _n_(61862, "print", lambda: print), 'Splitting ', _n_(61863, "nlist", lambda: nlist))
    _l_(61865)
    if _c_(61868, _n_(61866, "len", lambda: len), _n_(61867, "nlist", lambda: nlist)) > 1:
        _l_(61944)

        mid = _c_(61871, _n_(61869, "len", lambda: len), _n_(61870, "nlist", lambda: nlist)) // 2
        _l_(61872)
        lefthalf = _n_(61873, "nlist", lambda: nlist)[:_n_(61874, "mid", lambda: mid)]
        _l_(61875)
        righthalf = _n_(61876, "nlist", lambda: nlist)[_n_(61877, "mid", lambda: mid):]
        _l_(61878)
        _c_(61881, _n_(61879, "mergeSort", lambda: mergeSort), _n_(61880, "lefthalf", lambda: lefthalf))
        _l_(61882)
        _c_(61885, _n_(61883, "mergeSort", lambda: mergeSort), _n_(61884, "righthalf", lambda: righthalf))
        _l_(61886)
        i = j = k = 0
        _l_(61887)
        while _n_(61888, "i", lambda: i) < _c_(61891, _n_(61889, "len", lambda: len), _n_(61890, "lefthalf", lambda: lefthalf)) and _n_(61892, "j", lambda: j) < _c_(61895, _n_(61893, "len", lambda: len), _n_(61894, "righthalf", lambda: righthalf)):
            _l_(61917)

            if _n_(61896, "lefthalf", lambda: lefthalf)[_n_(61897, "i", lambda: i)] < _n_(61898, "righthalf", lambda: righthalf)[_n_(61899, "j", lambda: j)]:
                _l_(61914)

                _n_(61900, "nlist", lambda: nlist)[_n_(61901, "k", lambda: k)] = _n_(61902, "lefthalf", lambda: lefthalf)[_n_(61903, "i", lambda: i)]
                _l_(61904)
                i = _n_(61905, "i", lambda: i) + 1
                _l_(61906)
            else:
                _n_(61907, "nlist", lambda: nlist)[_n_(61908, "k", lambda: k)] = _n_(61909, "righthalf", lambda: righthalf)[_n_(61910, "j", lambda: j)]
                _l_(61911)
                j = _n_(61912, "j", lambda: j) + 1
                _l_(61913)
            k = _n_(61915, "k", lambda: k) + 1
            _l_(61916)
        while _n_(61918, "i", lambda: i) < _c_(61921, _n_(61919, "len", lambda: len), _n_(61920, "lefthalf", lambda: lefthalf)):
            _l_(61931)

            _n_(61922, "nlist", lambda: nlist)[_n_(61923, "k", lambda: k)] = _n_(61924, "lefthalf", lambda: lefthalf)[_n_(61925, "i", lambda: i)]
            _l_(61926)
            i = _n_(61927, "i", lambda: i) + 1
            _l_(61928)
            k = _n_(61929, "k", lambda: k) + 1
            _l_(61930)
        while _n_(61932, "j", lambda: j) < _c_(61935, _n_(61933, "len", lambda: len), _n_(61934, "righthalf", lambda: righthalf)):
            _l_(61943)

            _n_(61936, "nlist", lambda: nlist)[_n_(61937, "k", lambda: k)] = _n_(61938, "righthalf", lambda: righthalf)[_n_(61939, "j", lambda: j)]
            _l_(61940)
            j = _n_(61941, "j", lambda: j) + 1
            _l_(61942)
    _c_(61947, _n_(61945, "print", lambda: print), 'Merging ', _n_(61946, "nlist", lambda: nlist))
    _l_(61948)
nlist = [14, 46, 43, 27, 57, 41, 45, 21, 70]
_l_(61950)
_c_(61953, _n_(61951, "mergeSort", lambda: mergeSort), _n_(61952, "nlist", lambda: nlist))
_l_(61954)
_c_(61957, _n_(61955, "print", lambda: print), _n_(61956, "nlist", lambda: nlist))
_l_(61958)