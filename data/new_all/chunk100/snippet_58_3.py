# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def mergeSort(nlist):
    _l_(62145)

    _c_(62058, _n_(62056, "print", lambda: print), 'Splitting ', _n_(62057, "nlist", lambda: nlist))
    _l_(62059)
    if _c_(62062, _n_(62060, "len", lambda: len), _n_(62061, "nlist", lambda: nlist)) > 1:
        _l_(62140)

        mid = _c_(62065, _n_(62063, "len", lambda: len), _n_(62064, "nlist", lambda: nlist)) // 2
        _l_(62066)
        lefthalf = _n_(62067, "nlist", lambda: nlist)[:_n_(62068, "mid", lambda: mid)]
        _l_(62069)
        righthalf = _n_(62070, "nlist", lambda: nlist)[_n_(62071, "mid", lambda: mid):]
        _l_(62072)
        _c_(62075, _n_(62073, "mergeSort", lambda: mergeSort), _n_(62074, "lefthalf", lambda: lefthalf))
        _l_(62076)
        _c_(62079, _n_(62077, "mergeSort", lambda: mergeSort), _n_(62078, "righthalf", lambda: righthalf))
        _l_(62080)
        i = j = k = 0
        _l_(62081)
        while _n_(62082, "i", lambda: i) < _c_(62085, _n_(62083, "len", lambda: len), _n_(62084, "lefthalf", lambda: lefthalf)) and _n_(62086, "j", lambda: j) < _c_(62089, _n_(62087, "len", lambda: len), _n_(62088, "righthalf", lambda: righthalf)):
            _l_(62111)

            if _n_(62090, "lefthalf", lambda: lefthalf)[_n_(62091, "i", lambda: i)] < _n_(62092, "righthalf", lambda: righthalf)[_n_(62093, "j", lambda: j)]:
                _l_(62108)

                _n_(62094, "nlist", lambda: nlist)[_n_(62095, "k", lambda: k)] = _n_(62096, "lefthalf", lambda: lefthalf)[_n_(62097, "i", lambda: i)]
                _l_(62098)
                i = _n_(62099, "i", lambda: i) + 1
                _l_(62100)
            else:
                _n_(62101, "nlist", lambda: nlist)[_n_(62102, "k", lambda: k)] = _n_(62103, "righthalf", lambda: righthalf)[_n_(62104, "j", lambda: j)]
                _l_(62105)
                j = _n_(62106, "j", lambda: j) + 1
                _l_(62107)
            k = _n_(62109, "k", lambda: k) + 1
            _l_(62110)
        while _n_(62112, "i", lambda: i) < _c_(62115, _n_(62113, "len", lambda: len), _n_(62114, "lefthalf", lambda: lefthalf)):
            _l_(62125)

            _n_(62116, "nlist", lambda: nlist)[_n_(62117, "k", lambda: k)] = _n_(62118, "lefthalf", lambda: lefthalf)[_n_(62119, "i", lambda: i)]
            _l_(62120)
            i = _n_(62121, "i", lambda: i) + 1
            _l_(62122)
            k = _n_(62123, "k", lambda: k) + 1
            _l_(62124)
        while _n_(62126, "j", lambda: j) < _c_(62129, _n_(62127, "len", lambda: len), _n_(62128, "righthalf", lambda: righthalf)):
            _l_(62139)

            _n_(62130, "nlist", lambda: nlist)[_n_(62131, "k", lambda: k)] = _n_(62132, "righthalf", lambda: righthalf)[_n_(62133, "j", lambda: j)]
            _l_(62134)
            j = _n_(62135, "j", lambda: j) + 1
            _l_(62136)
            k = _n_(62137, "k", lambda: k) + 1
            _l_(62138)
    _c_(62143, _n_(62141, "print", lambda: print), 'Merging ', _n_(62142, "nlist", lambda: nlist))
    _l_(62144)
_c_(62148, _n_(62146, "mergeSort", lambda: mergeSort), _n_(62147, "nlist", lambda: nlist))
_l_(62149)
_c_(62152, _n_(62150, "print", lambda: print), _n_(62151, "nlist", lambda: nlist))
_l_(62153)