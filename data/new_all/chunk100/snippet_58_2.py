# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def mergeSort(nlist):
    _l_(62046)

    _c_(61961, _n_(61959, "print", lambda: print), 'Splitting ', _n_(61960, "nlist", lambda: nlist))
    _l_(61962)
    if _c_(61965, _n_(61963, "len", lambda: len), _n_(61964, "nlist", lambda: nlist)) > 1:
        _l_(62041)

        mid = _c_(61968, _n_(61966, "len", lambda: len), _n_(61967, "nlist", lambda: nlist)) // 2
        _l_(61969)
        lefthalf = _n_(61970, "nlist", lambda: nlist)[:_n_(61971, "mid", lambda: mid)]
        _l_(61972)
        righthalf = _n_(61973, "nlist", lambda: nlist)[_n_(61974, "mid", lambda: mid):]
        _l_(61975)
        _c_(61978, _n_(61976, "mergeSort", lambda: mergeSort), _n_(61977, "lefthalf", lambda: lefthalf))
        _l_(61979)
        _c_(61982, _n_(61980, "mergeSort", lambda: mergeSort), _n_(61981, "righthalf", lambda: righthalf))
        _l_(61983)
        i = j = k = 0
        _l_(61984)
        while _n_(61985, "i", lambda: i) < _c_(61988, _n_(61986, "len", lambda: len), _n_(61987, "lefthalf", lambda: lefthalf)) and _n_(61989, "j", lambda: j) < _c_(61992, _n_(61990, "len", lambda: len), _n_(61991, "righthalf", lambda: righthalf)):
            _l_(62014)

            if _n_(61993, "lefthalf", lambda: lefthalf)[_n_(61994, "i", lambda: i)] < _n_(61995, "righthalf", lambda: righthalf)[_n_(61996, "j", lambda: j)]:
                _l_(62011)

                _n_(61997, "nlist", lambda: nlist)[_n_(61998, "k", lambda: k)] = _n_(61999, "lefthalf", lambda: lefthalf)[_n_(62000, "i", lambda: i)]
                _l_(62001)
                i = _n_(62002, "i", lambda: i) + 1
                _l_(62003)
            else:
                _n_(62004, "nlist", lambda: nlist)[_n_(62005, "k", lambda: k)] = _n_(62006, "righthalf", lambda: righthalf)[_n_(62007, "j", lambda: j)]
                _l_(62008)
                j = _n_(62009, "j", lambda: j) + 1
                _l_(62010)
            k = _n_(62012, "k", lambda: k) + 1
            _l_(62013)
        while _n_(62015, "i", lambda: i) < _c_(62018, _n_(62016, "len", lambda: len), _n_(62017, "lefthalf", lambda: lefthalf)):
            _l_(62028)

            _n_(62019, "nlist", lambda: nlist)[_n_(62020, "k", lambda: k)] = _n_(62021, "lefthalf", lambda: lefthalf)[_n_(62022, "i", lambda: i)]
            _l_(62023)
            i = _n_(62024, "i", lambda: i) + 1
            _l_(62025)
            k = _n_(62026, "k", lambda: k) + 1
            _l_(62027)
        while _n_(62029, "j", lambda: j) < _c_(62032, _n_(62030, "len", lambda: len), _n_(62031, "righthalf", lambda: righthalf)):
            _l_(62040)

            _n_(62033, "nlist", lambda: nlist)[_n_(62034, "k", lambda: k)] = _n_(62035, "righthalf", lambda: righthalf)[_n_(62036, "j", lambda: j)]
            _l_(62037)
            k = _n_(62038, "k", lambda: k) + 1
            _l_(62039)
    _c_(62044, _n_(62042, "print", lambda: print), 'Merging ', _n_(62043, "nlist", lambda: nlist))
    _l_(62045)
nlist = [14, 46, 43, 27, 57, 41, 45, 21, 70]
_l_(62047)
_c_(62050, _n_(62048, "mergeSort", lambda: mergeSort), _n_(62049, "nlist", lambda: nlist))
_l_(62051)
_c_(62054, _n_(62052, "print", lambda: print), _n_(62053, "nlist", lambda: nlist))
_l_(62055)